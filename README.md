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

- [x] Describe the game's purpose.
The game's purpose is for the player to guess the secret number within the number of attempts. If the player is playing is easy mode, the number of attempts is 6. If the player is playing normal mode, the number of attempts is 8. For the difficult mode, the number of attempts is 5.

- [X] Detail which bugs you found.
1. The hint would print "Too high" when secret number is higher than the guess, and vice versa.
2. The "New Game" button does not work
3. When switching difficulty, nothing changes in the game.
4. The number of attempts start from 1, so total number of attempts would be allowed attempts - 1.
5. The score is not calcualted correctly. The even attempts give +5 points if the wrong guess is made.
6. Resolve the type error problem. 
- [X] Explain what fixes you applied.
1. The conditional logic was swapped to fix the hint printing out the wrong message.
2. Statements are inserted to reset the values of all variables including attempts, score, and history.
3. The statements to reset all variables when the difficulty changed is added, and ensured the secret number generated is within the correct range.
4. The value saved to attempts were changed from 1 to 0 when the game starts or resets.
5. The condition where it checks if the attempt is even attempt, if it is +5 points to the total score is removed. The line where it states +5 points to total score is also removed.
6. Under the else clause, remove the conversion of secret value into a string. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the project folder path in terminal and run "python -m streamlit run app.py"
2. Choose the difficulty you want to play
3. Enter a number in the "Enter your guess:" field.
4. Press "Enter" key.
5. Press "Submit Guess" button.
6. A hint will pop up telling the paper to choose a higher or lower number.
7. The cycle will repeat from step 3 to step 5. Until the player reaches the max number of attempts or the player guess the correct number.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
