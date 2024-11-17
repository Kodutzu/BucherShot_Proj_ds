import random
from Sounds.music import sound_effect
import json

line = "--------------------------------"



with open('./Settings.json', 'r') as f:
        data = json.load(f)


def mag_set(size, live_ratio=data["live_ratio"]):

    
    # Calculate the number of live bullets based on the ratio
    
    live_count = max(1, int(size*live_ratio))  # Ensure at least 1 live bullet
    blank_count = size - live_count

    # Create the magazine with the required number of live and blank bullets
    mag = [1] * live_count + [0] * blank_count

    # Shuffle the magazine for randomness
    random.shuffle(mag)
    
    return mag

def load(Shotgun):
    shell = random.choice(Shotgun)
    
    return shell

def fire(player, shell , players_charge):
    
   
        if shell == 1:
            sound_effect(data["Sound_effect"]["Live"], data["Sound_effect"]["Volume"])
            print(f"fired a live shell! 💥BOOM💥 ! {player} lost one 🪫 ")
            players_charge[player] -= 1  # Reduce the player's hearts
             # Player loses
        elif shell == 0:

            sound_effect(data["Sound_effect"]["Blank"], data["Sound_effect"]["Volume"])
            print(f"fired a blank shell. {player} is Safe! ✅")

        else:
            pass


    
        return players_charge, shell # Player survives

def mag_checker(shotgun):
    # Return False if there are no live or blank bullets left
    if not shotgun or shotgun.count(1) == 0 or shotgun.count(0) == 0:
        return 0
    return 1
    
def print_mag(shotgun):

    dis_shotgun = sorted(shotgun, reverse=True)
    print("here's Your current Line-up \n")

    for bullet in dis_shotgun:
        
        if(bullet == 1):
            print("🔴", end=" ")
            
        elif(bullet == 0):
            print("🟢", end=" ")

    print("\n\n")
    print("Total Live Bullet: ", shotgun.count(1))
    print("Total Blank Bullet: ", shotgun.count(0))

def print_stats(shotgun, player_charge):
    
    # After Bullet shot!
    print(line * 2 )
    for player, charge in player_charge.items():
        print(f"Player: ", player, " | Charge:", "🔋"*charge )
        

    print(line * 2)

