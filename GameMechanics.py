import random

def mainGame(P1Charge, P2Charge, mag_size):


    shotgun = mag_set(mag_size)
    

    player_charge = {"you": P1Charge , "nigga": P2Charge} 
    plist = list(player_charge)
    
    turn = 0
    

    while (turn <= len(shotgun)):

        print_mag(shotgun)
        loader, shotgun = load(shotgun)
        current_player = plist[turn%2]
        print(f"\n{current_player}'s turn!")
        target = input("Nigga or You?: ")
        
        fire(target,loader,player_charge, shotgun) #remove shotgun, Don't forget!
       

        
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
    Shotgun[selector] = -1
    return shell, Shotgun

def fire(player, shell , players_charge, shotgun):
    
    if shell == 1:
        print(f"{player} fired a live shell! BOOM! -1 heart")
        players_charge[player] -= 1  # Reduce the player's hearts
        if players_charge[player] <= 0:
            print(f"{player} has no hearts left!")
            return False  # Player loses
    elif shell == 0:
        print(f"{player} fired a blank shell. Safe!")

    print("-----------------------")
    print("Player Charge: ",players_charge[player], " | Shotgun Mags:" , shotgun )
    print("-----------------------")

    
    return True  # Player survives

def print_mag(shotgun):

    total_live = 0
    total_blank = 0
    print("here's Your current Line-up \n")

    for bullet in shotgun:
        
        if(bullet == 1):
            print("{L}", end=" ")
            total_live += 1
            
        elif(bullet == 0):
            print("(B)", end=" ")
            total_blank += 1

    print("\n\n")
    print("Total Live Bullet: ", total_live)
    print("Total Blank Bullet: ", total_blank)

if __name__ == "__main__":
    mainGame(3,3,8)