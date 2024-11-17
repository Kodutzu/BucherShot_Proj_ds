import Computer, time
from Mechanics_Level.GameMechanics import *
import json

with open('./Settings.json', 'r') as f:
        data = json.load(f)

def mainGame(player_charge, mag_size):
    shotgun = mag_set(mag_size)
    turn = 0
    plist = list(player_charge)

    while len(shotgun) != 0:
        if mag_checker(shotgun) != 1:
            return 0, " "

        for player, charge in player_charge.items():
            if charge <= 0:
                return -1, player

        shell = load(shotgun)
        current_player = plist[turn % len(plist)]

        print_mag(shotgun)

        print(f"\n{current_player}'s turn!")
        

        if current_player == plist[0]:
            print(f"Available targets: {plist}")
            user_target = input(f"Who do you want to shoot?: ").lower()

            if user_target not in plist:
                print("\nInvalid target. Skipping turn.")
                time.sleep(2)
                turn += 1
                continue
            
            
            time.sleep(3)
            fire(user_target, shell, player_charge)
            if(shell == 0 and current_player == user_target):
            
                print(f"{current_player} will Shoot Again!")
                turn +=1

            time.sleep(4)  # Add delay before the next turn
        else:
            print(f"{current_player} is thinking 💭..., let him cook!🍳")

            time.sleep(3)  # Simulate bot decision-making

            bot_target = Computer.bot(current_player, player_charge, plist, shotgun)

            if(current_player == bot_target):
                print(f"{current_player} chooses to shoot itself.")
            else:
                print(f"{current_player} chooses to shoot {bot_target}.")
             
            time.sleep(1)
            
           
            fire(bot_target, shell, player_charge)
            if(shell == 0 and current_player == bot_target):
                print(f"{current_player} will shoot again!")
                turn +=1

            time.sleep(4)  # Add delay before the next turn

        turn += 1
        shotgun.remove(shell)

        print_stats(shotgun, player_charge)
        time.sleep(4)  # Add delay before the next turn

if __name__ == "__main__":
    mainGame()