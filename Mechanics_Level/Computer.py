import random, json

with open('./Settings.json', 'r') as f:
    data = json.load(f)

def bot(player_name, player_charge, plist, shotgun):

    # Count live and blank bullets
    live_count = shotgun.count(1)
    total_bullets = len(shotgun)
    live_prob = live_count / total_bullets
    blank_prob = 1 - live_prob


    # The Bot includes itself as a possible target

    # Identify the opponent
    opponent = plist[0]

    # Bot's and opponent's charges
    bot_charges = player_charge[player_name]
    opponent_charges = player_charge[opponent]

   
   # Risk thresholds
    critical_health = data["Bot"]["Critical_health"]  # Bot is in danger when charges reach this value
    aggressive_threshold = data["Bot"]["Aggressive_threshold"]   # Probability at which bot becomes aggressive

    # Decision-making
    if live_prob > blank_prob:  # More likely to draw a live bullet
        
        if bot_charges > critical_health and opponent_charges < bot_charges:
            # Bot has more charges than opponent, prioritize attacking
            target = opponent

        elif bot_charges <= critical_health:

            # Bot is at critical health, avoid shooting itself
            target = opponent

        else:
            # Neutral stance, attack opponent
            target = opponent
    elif live_prob < blank_prob:  # More likely to draw a blank bullet
        if bot_charges <= critical_health:
            # Gamble on shooting opponent to stay in the game
            target = opponent

        elif blank_prob > aggressive_threshold:
            # Bot feels safe shooting itself
            target = player_name
        else:
            # Default to attacking opponent
            target = opponent

    else:  # Neutral probabilities

        if bot_charges == opponent_charges:

            # Avoid a draw by taking a calculated risk
            target = random.choice([player_name, opponent])

        elif bot_charges < opponent_charges:

            # Bot is losing, go aggressive
            target = opponent
        else:

            # Bot is winning, play it safe
            target = player_name
    

 

    return target