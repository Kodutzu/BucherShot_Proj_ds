import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
from pygame import mixer



def background_music(volume=0.2, track = "./Music&Sound_Effects/Buckshot_mini_SE.mpeg"):
    
    mixer.init()

    # Load the music file
    mixer.music.load(track)

    # Set volume
    mixer.music.set_volume(volume)

    # Play the music in a loop
    mixer.music.play(loops=-1)  # -1 means the music will loop indefinitely
    

def music_stop():

    mixer.music.stop()

# Function to play a one-time sound effect
def sound_effect(SE_path, volume=0.7):
    sound_effect = mixer.Sound(SE_path)
    sound_effect.set_volume(volume)
    sound_effect.play()
        
       

