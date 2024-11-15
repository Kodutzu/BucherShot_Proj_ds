import random, Computer

line = "-------------------------------- \n"

def mainGame(player_charge, mag_size):
    # Initialize the game state
    shotgun = mag_set(mag_size)
    turn = 0

    plist = list(player_charge)

    while len(shotgun) != 0:
        if mag_checker(shotgun) != 1:
            print(line)
            print("\nIt's a tie!")
            break

        print_mag(shotgun)
        loader, shotgun = load(shotgun)  # Load the next shell
        current_player = plist[turn % len(plist)]  # Alternate between players

        print(f"\n{current_player}'s turn!")

        if current_player == 'you':
            # Player turn
            print(line)
            print(f"Available targets: {plist}")
            target = input(f"Who do you want to shoot?: ")

            # Validate target
            if target not in plist:
                print(line)
                print("Invalid target. Skipping turn.")
                turn += 1
                continue

            fire(target, loader, player_charge)
            print(player_charge)

        else:
            # AI turn
            ai_target = Computer.bot(current_player, player_charge, plist, shotgun)  
            print(line)
            print(f"{current_player} chooses to shoot {ai_target}.")
            fire(ai_target, loader, player_charge)
            print(player_charge)

        # Check for game end conditions
        for player, charge in player_charge.items():
            if charge <= 0:
                print(line)
                print(f"Game ends! {player} ran out of charges!")
                return  # Exit the game loop and end the function

        turn += 1

    else:
        print("\nBoth players survived. It's a draw!")


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
    selector = random.randint(0, len(Shotgun)-1)
    shell = Shotgun[selector]
    Shotgun.pop(selector) 
    return shell, Shotgun

def fire(player, shell , players_charge):
    
   
        if shell == 1:
            print(f"{player} fired a live shell! BOOM! -1 heart")
            players_charge[player] -= 1  # Reduce the player's hearts
             # Player loses
        elif shell == 0:
            print(f"{player} fired a blank shell. Safe!")

        else:
            pass


    
        return players_charge  # Player survives

def mag_checker(shotgun):

    no_of_live = 0
    no_of_blank = 0
    for bullet in shotgun:
        if(bullet == 1 ):
            no_of_live+=1

        else:
            no_of_blank +=1

    if((no_of_live ==0) or (no_of_blank== 0) ):    
         return 0
    else:
        return 1
    
    

def print_mag(shotgun):

    total_live = shotgun.count(1)
    total_blank = shotgun.count(0)
    print("here's Your current Line-up \n")

    for bullet in shotgun:
        
        if(bullet == 1):
            print("{L}", end=" ")
            
        elif(bullet == 0):
            print("(B)", end=" ")

    print("\n\n")
    print("Total Live Bullet: ", total_live)
    print("Total Blank Bullet: ", total_blank)

def print_stats(shotgun, player_charge):
    
    # After Bullet shot!
    print(line)
    print(player_charge, " | " , "Mags: " ,shotgun, end = "\n\n")
    print(line)

if __name__ == "__main__":
    mainGame()