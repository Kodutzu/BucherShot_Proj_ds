# Buckshot Roulette Mini!
My friend and I built this game as a school project. It’s a two-player game with strategic decision-making!

## About the Game
This is my best programming project to date, completed in 3 days!
There’s also a Settings.json file for easy customization.

## Features
Two-player mode (Player vs. Bot).
Customizable settings.
Immersive background music and sound effects.

## Installation

1. Download The Repository, Unzip it!
2. Then Search Buchershot.py and Open it in your IDE!
3. Then Go to Terminal and type -: `pip install -r requirements.txt`
4. And Then Finally Type -: `python buckshot.py` in Terminal - (Basically run the program)

## **How to Play BucherShot Mini**

Here’s a step-by-step guide to help you play your mini version of Buckshot Roulette:

---

### **Objective**:
Survive the round while strategically managing your decisions. Either shoot yourself or the opponent (Bot) and hope the shell is a blank. The last player standing wins.

---

### **Game Setup**:

2. **Players**:
   - **You**: The human player.
   - **Opponent (Bot) **: A computer bot making strategic decisions.

3. **Shotgun Magazine**:
   - Contains a randomized mix of live (🔴) and blank (🟢) shells.
   - The shells are drawn randomly during each turn.

---

### **Gameplay**:

1. **Mechanics**:
   - The game alternates turns between you and the Bot.
   - On your turn, you choose whether to:
     - **Shoot Yourself**: Risk a blank shell to save your opponent's charges.
     - **Shoot the Opponent (AI)**: Risk a live shell to damage your opponent's charges.

2. **Player’s Turn**:
   - The magazine lineup is displayed (e.g., `🔴🟢🔴 `).
   - Choose your target:
     - Type **"username"** to shoot yourself.
     - Type **"botname"** to shoot the AI opponent.
   - The shotgun loads a random shell, and the result (live or blank) is revealed.

3. **Bot’s Turn**:
   - The Bot assesses the probability of live and blank shells.
   - It also considers your charges and its own before deciding whom to shoot.
   - The Bot announces its decision (self or opponent) and takes the shot.

---

### **Winning the Game**:
- If a player’s charges drop to **0** after a live shell hits, the game ends:
  - **If Bot’s charges drop to 0**: **You Win! 🎉**
  - **If your charges drop to 0**: **Bot Wins. 💀**
- If all bullets are used and both players still have charges, the game ends in a **Draw**.

---

### **Game Tips**:
1. **Manage Risk**:
   - If there are more blanks than live bullets, consider shooting yourself to avoid a live shot on your opponent.
   - If live bullets dominate, try shooting the opponent.
     
2. **Keep an Eye on Charges**:
   - Protect your charges while aiming to deplete the opponent’s.

3. **Monitor the Magazine**:
   - Use the displayed magazine to estimate probabilities and plan your strategy.

---

### **Troubleshooting**:
- If the game doesn’t run, ensure to run `pip install -r requirements.txt`.
- Check the `Settings.json` file for valid configurations.
- Report any bugs or unexpected behaviours.

---

Enjoy the thrill of BucherShot Mini! 🥳


## Libraries:

Pygame for sound effects.
JSON for settings customization.

