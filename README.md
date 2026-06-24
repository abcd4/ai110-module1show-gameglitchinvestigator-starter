# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game's purpose is to allow users to guess a secret number within 8 attempts, while providing hints along the way that help the user make new guesses.
- A key bugs that I found were that the hints that the game provided were the opposite of what the user should guess. Additionally, I found that when a number out of the game's range was guessed, there was no message indicating that the user had made a guess out of the range.
- To fix the hint bug, I fixed the logic so that when a guess is to high, it hints the user to make a lower guess and vice versa. To fix the out of range bug, I added a check that ensured that the user's guess was within 1 and 100 inclusive. If it wasn't, the user would receive a message indicating so.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 8
2. Game returns "Too Low"
3. User enters a guess of 70
4. Game returns "Too High"
5. User enters a guess of 58
6. Game ends with correct guess an provides a final score

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
First time: 
 % python -m pytest
============================= test session starts ==============================
platform darwin -- Python 3.12.4, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/nicoleonye/ai110-module1show-gameglitchinvestigator-starter
collected 5 items                                                              

tests/test_game_logic.py .....                                           [100%]

============================== 5 passed in 0.01s ===============================


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
