# Buckshot Roulette Mini!
My friend and I built this game as a school project. It’s a two-player game with strategic decision-making!

## About the Game
This is my best programming project to date, completed in 3 days!

## Installation

1. Download The Repository, Unzip it!
2. Then Search Buckshot.py and Open it in your IDE!
3. Then Go to Terminal and type -: `pip install -r requirements.txt`
4. And Then Finally Type -: `python buckshot.py` in Terminal - (Basically run the program)

## **How to Play Buckshot Mini**

Here’s a step-by-step guide to help you play your mini version of Buckshot Roulette:

---

### **Objective**:
Survive the round while strategically managing your decisions. Either shoot yourself or the opponent (Bot) and hope the shell is a blank. The last player standing wins.

---

### **Game Setup**:

1. **Players**:
   - **You**: It's literally you!.
   - **Opponent (Bot)**: A computer bot making strategic decisions.

2. **Shotgun Magazine**:
   - Contains a randomized mix of live (🔴) and blank (🟢) shells.
   - The shells are drawn randomly during each turn.

### **Gameplay**:

1. **Overall Concept**:  
   - The game revolves around a shotgun loaded with two types of shells:  
     - **Live Bullets** (`🔴`): Dangerous and can deplete a player’s charges.  
     - **Blank Bullets** (`🟢`): Harmless but add suspense to the game.  
   - Players take turns firing the shotgun, aiming either at themselves or the opponent (the Bot).  
   - The goal is to manage risk while trying to deplete the opponent’s charges.

---

2. **Game Mechanics**:  
   - **Turns**:  
     - The game alternates between the Player and the Bot.  
     - Each turn involves loading the shotgun with a randomly selected bullet and firing it.  
   - **Choices**:  
     - On your turn, you decide whom to shoot:
       - **Shoot Yourself**: Take the risk, hoping for a blank bullet 
       - **Shoot the Bot**: Risk firing a live bullet to reduce the Bot’s charges.
   - The game ends when one player's charges reach zero or when all bullets are used.  

---

3. **Player’s Turn**:  
   - **Magazine Display**:  
     The lineup of the magazine (e.g., `🔴🟢🔴`) is displayed, providing insight into the remaining live and blank bullets.  
   - **Target Selection**:  
     - Type your username (e.g., `"you"`) to shoot yourself.  
     - Type `"botname"` to shoot the AI opponent.  
   - **Random Shot**:  
     The shotgun randomly selects a shell from the magazine.  
     - If the shell is live (`🔴`), the target loses one charge.  
     - If the shell is blank (`🟢`), nothing happens.
      
   - **Feedback**:  
     After the shot, the game updates you on:
     - Who was shot.  
     - The type of bullet fired.  
     - Remaining charges for both players.  

---

4. **Bot’s Turn**:  
   - The Bot makes decisions based on probabilities:
     - It calculates the likelihood of live (`🔴`) vs. blank (`🟢`) bullets based on the remaining shells.  
     - It also considers the current charges for both players.
       
   - **Decision Logic**:  
     - If live bullets dominate: The Bot might target you to deplete your charges.  
     - If blanks dominate: The Bot may target itself, preserving its charges.  
     - If probabilities are equal: The Bot might make a random decision, adding unpredictability to the game.
        
   - The Bot announces its target and fires.
  
### _Important: if you shoot yourself with a blank bullet, then you will be given another chance to shoot! This also applies for the bot_

---

5. **Winning the Game**:  
   - The game ends immediately if a player’s charges drop to zero after a live shell hits.  
     - **If the Bot’s charges drop to 0**: You win! 🎉  
     - **If your charges drop to 0**: The Bot wins. 💀
       
   - If all bullets are used and both players still have charges, the game ends in a **Draw**.
   - If Only Live bullet or Only Blank are left in the Magazine, then the game ends in a **Draw** again.

---

## **Settings Customization**

You can configure the gameplay, sound, and bot behavior by editing the `Settings.json` file. This allows you to tailor the game to your preferences. Below is a breakdown of each setting and its purpose:

---

#### **Game Parameters**
- **`No_of_userCharges`**:  
  - The number of charges (lives) the player starts with.  
  - Example: `"No_of_userCharges": 3` gives you 3 Charges.  
  - Increase or decrease this value to make the game easier or harder for yourself.

- **`No_of_botCharges`**:  
  - The number of charges (lives) the Bot starts with.  
  - Example: `"No_of_botCharges": 3` gives the Bot 3 Charges.  
  - Adjust this value to balance the difficulty.

- **`No_of_Bullets`**:  
  - The total number of bullets (live + blank) in the magazine.  
  - Example: `"No_of_Bullets": 16` means 16 bullets in the game.  
  - A higher number increases the game's length, while a lower number makes it shorter and more intense.

- **`live_ratio`**:  
  - The proportion of live bullets to total bullets.  
  - Example: `"live_ratio": 0.5` means 50% of the bullets are live, and the remaining 50% are blank.  
  - Adjust this value to control the danger level:
    - **Higher Ratio (e.g., 0.7)**: More live bullets, making the game riskier.  
    - **Lower Ratio (e.g., 0.3)**: More blank bullets, reducing the risk.

---

#### **Sound and Music Settings**
- **`Background Music`**:  
  - Customize the music that plays during the game.  
    - **`Track`**: The path to the music file. You can replace this with any compatible file path.  
      - Example: `"Track": "./Music_SoundEffects/Music/Your_Track_Name"`.
        
   - **`Volume`**: Set the volume of the background music (0.0 to 1.0).
   -   
      - Example: `"Volume": 0.3` sets the music volume to 30%.

   - Replace `Your_Track_Name` with the name of your Track.

- **`Sound_effect`**:
  - Define sound effects for specific game events:
    - **`Blank`**: The sound effect for a blank shot.  
      - Example: `"Blank": "./Music_SoundEffects/Sound_effects/Your_SoundEffect_Name"`.  
    - **`Live`**: The sound effect for a live shot.  
      - Example: `"Live": "./Music_SoundEffects/Sound_effects/Your_SoundEffect_Name"`.  
    - **`Victory`**: The sound effect for victory.  
      - Example: `"Victory": "./Music_SoundEffects/Sound_effects/Your_SoundEffect_Name"`.  
    - **`Volume`**: Set the volume for sound effects (0.0 to 1.0).  
      - Example: `"Volume": 0.7` sets sound effect volume to 70%.
        
  - Replace `Your_SoundEffect_Name` with the name of your Sound Effect

---

#### **Bot Behavior**
- **`Bot`**:  
  - Configure the Bot's decision-making strategy:
    - **`Aggressive_threshold`**:  
      - Determines the probability threshold for aggressive behaviour.  
      - Example: `"Aggressive_threshold": 0.5` means the Bot becomes aggressive when live bullets are more likely than blanks.  
      - Lower values make the Bot more defensive, while higher values make it more aggressive.  
    - **`Critical_health`**:  
      - The charge count at which the Bot considers itself critically endangered and adjusts its strategy.  
      - Example: `"Critical_health": 1` means the Bot becomes cautious when its charges drop to 1.


---

### **Game Tips**:
1. **Risk Management**:  
   - Don’t shoot yourself if live bullets dominate the magazine.  
   - When blanks dominate, it’s safer to shoot yourself to avoid giving your opponent an advantage.  

2. **Analyze Probabilities**:  
   - Watch the magazine lineup and remaining bullets to anticipate the odds of drawing a live shell.  

3. **Play Aggressively or Defensively**:  
   - Target the Bot early if you feel confident about the odds.  
   - Play defensively and conserve charges if you’re falling behind.  

---
### Troubleshooting:

1. If the game doesn’t run, ensure to run `pip install -r requirements.txt` in your terminal!
2. Check the Settings.json file for valid configurations.

Enjoy **Buckshot Mini**! 


