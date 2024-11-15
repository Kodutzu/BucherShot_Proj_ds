import random, Computer, time
from music import sound_effect

line = "--------------------------------"

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
            user_target = input(f"Who do you want to shoot?: ")

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


def mag_set(size, live_ratio=0.5):

    
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
            sound_effect('./Music&Sound_Effects/desert-eagle-gunshot.wav', 0.7)
            print(f"fired a live shell! 💥BOOM💥 ! {player} lost one 🪫 ")
            players_charge[player] -= 1  # Reduce the player's hearts
             # Player loses
        elif shell == 0:

            sound_effect( './Music&Sound_Effects/happy.wav',0.7)
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

if __name__ == "__main__":
    mainGame()