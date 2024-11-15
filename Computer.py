import random, GameMechanics


def bot(player_name, player_charge, plist, shotgun):

    # Count live and blank bullets
    live_count = shotgun.count(1)
    total_bullets = len(shotgun)
    live_prob = live_count / total_bullets
    blank_prob = 1 - live_prob


    # The AI includes itself as a possible target
    
    targets = plist

    # Identify the opponent
    opponent = max([player for player in targets if player != player_name], 
                   key=lambda player: player_charge[player])

    # AI's and opponent's charges
    ai_charges = player_charge[player_name]
    opponent_charges = player_charge[opponent]

   
    # Decision-making
    if live_prob > blank_prob:  # More likely to draw a live bullet
        if opponent_charges < ai_charges:

             target = player_charge  # Prioritize attacking opponent

        else:
              target = opponent
               
        
    elif(live_prob < blank_prob):  # More likely to draw a blank bullet
            target = player_name  
    else :
            target = random.choice(targets)
    

 

    return target