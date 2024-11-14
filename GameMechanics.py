import random



def mainGame():

    
    inv = inv_set(8)

    print("Welcome to Buckshot Roulette!")
    shotgun = load_shotgun(inv)
    turn = 0
    players = ["Pc_1", "Pc_2"]
    
    while turn < len(shotgun):
        current_player = players[turn % 2]
        print(f"\n{current_player}'s turn:")
        
        # Optional: Allow player to take actions
        if current_player == "Pc_1":
            input("Press Enter to pull the trigger...")
        
        # Fire the shotgun
        if not fire_shot(current_player, shotgun, turn):
            print(f"{current_player} lost the game!")
            break
        
        turn += 1

    else:
        print("\nBoth players survived. It's a draw!")



def inv_set(size):

    inv = dict()
    live_blank = ("live", "blank")
    for i in range(1, size+1):
        sequencer = random.randint(0,len(live_blank)-1)
        inv.update({i: live_blank[sequencer]})

    return inv

def load_shotgun(inv):
    selector = random.randint(1, len(inv))
    return inv.get(selector)
    

def fire_shot(player, shotgun, turn):
    shell = shotgun[turn]
    if shell == 1:
        print(f"{player} fired a live shell! BOOM!")
        return False  # Player loses
    else:
        print(f"{player} fired a blank shell. Safe!")
        return True  # Player survives


if __name__ == "__main__":
    mainGame()