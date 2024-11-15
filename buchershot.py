import GameMechanics
from music import background_music
import time

def main():
    user, bot = loading_screen()
    player_charge = {user: 3, bot: 3}

    while(True):

        time.sleep(2)
        background_music()
        game_result, losing_player = GameMechanics.mainGame(player_charge, 15)
        

        if game_result == 0:
            print("\nIt's a Tie! No bullets left.")
            break;
        elif game_result == -1:
            print(f"\nGame ends! {losing_player} ran out of charges!")
            break;
            

def loading_screen():
    """Displays a loading screen with delays."""
    print("Welcome to our Mini Buchershot Game!")
    time.sleep(1)

    username = input("Enter your name: ")
    botname = input("Name Your Bot: ")

    print("\nLoading Your Game", end=" ")
    for _ in range(5):  # Simulate loading with dots
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")

    return username, botname


main()