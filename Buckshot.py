import Mechanics_Level.Level_one as l1
from Music_SoundEffects.music  import background_music as bgm , sound_effect, music_stop
import json
import time

def main():

    with open('./Settings.json', 'r') as f:
        data = json.load(f)
    

    user, bot = loading_screen()
    player_charge = {user: data["No_of_userCharges"], bot: data["No_of_botCharges"]}


    while(True):

        time.sleep(2)
        bgm(data["Background Music"]["Volume"], data["Background Music"]["Track"])
        game_result, losing_player = l1.mainGame(player_charge,data["No_of_Bullets"]  )
        

        if game_result == 0:
            print("\nIt's a Tie! No bullets left.")
            break;
        elif game_result == -1:
            
             
            music_stop()
            sound_effect(data["Sound_effect"]["Victory"], data["Sound_effect"]["Volume"])
            print(f"\nGame ends! {losing_player} ran out of charges!")
            time.sleep(5)
            
            break;
        
   

def loading_screen():

    while(True):
        username = input("Enter your name: ").lower()
        botname = input("Name Your Bot: ").lower()

        if(username == botname):
            print("💥Error, You can't have same name for Bot")
            print()
        else:
            break;
    
        """Displays a loading screen with delays."""
  
    Banner = """

██████╗ ██╗   ██╗ ██████╗██╗  ██╗███████╗██╗  ██╗ ██████╗ ████████╗    ███╗   ███╗██╗███╗   ██╗██╗
██╔══██╗██║   ██║██╔════╝██║ ██╔╝██╔════╝██║  ██║██╔═══██╗╚══██╔══╝    ████╗ ████║██║████╗  ██║██║
██████╔╝██║   ██║██║     █████╔╝ ███████╗███████║██║   ██║   ██║       ██╔████╔██║██║██╔██╗ ██║██║
██╔══██╗██║   ██║██║     ██╔═██╗ ╚════██║██╔══██║██║   ██║   ██║       ██║╚██╔╝██║██║██║╚██╗██║██║
██████╔╝╚██████╔╝╚██████╗██║  ██╗███████║██║  ██║╚██████╔╝   ██║       ██║ ╚═╝ ██║██║██║ ╚████║██║
╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝       ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝
                                                                                                                  
"""
    time.sleep(1)
    print(Banner)

    print("\nLoading Your Game", end=" ")
    for _ in range(5):  # Simulate loading with dots
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")

    return username, botname


main()