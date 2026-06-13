# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  In the Developer Debug Info, it shows Secret:1, Attempts: 1, Score: 0, Difficulty: Normal, History: []
  However, on the left side it shows attempts allowed is 8.
  On the left side also show that the difficulty can be changed.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The attempts values should start from 0, because no attempts had been made in the start.
  When switching the difficulty level, the secret value does not change to match difficulty, the instructions on top does not change depeding on difficulty level. 
  

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|50| Go Lower |  Go HIGHER |       None |
| | After pressing new game, everything should refresh. | Only the secret number resets | None|
|50| When a wrong number is entered, score should be subtracted. |Some values add scores and other subtract. | None |
 13 | I tried to guess correctly at the last attempt. Results should give me correct. | Only allowed 7 attempts. | None |
|25| Go HIGHER| Go Lower| Not thrown but there is a type error.|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 

Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I started with a simple issue where the number of attempts start with 1 eventhough no attempts has been made. AI helped pointed out which line in app.py caused this issue. The result is verified by running the project, and testing if a player has 8 attempts on normal mode.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

When I asked the AI coding assistant for suggestion on fixing the "New Game" button not working issue. AI pointed out the lines this problem was on, and suggested solutions. It set the attempts to start at 1. If the "new game" button is pressed, the player now only have 7 attempts instead of 8. I verified the result by running the project and testing if the new function is fixed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? 

The way I decide if a bug is really fixed is by running the project again. I reenact the scene again to make sure the outcome is correct. If the outcome is the expected outcome, then the bug is fixed. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  The test I ran included test_guess_too_high(), and test_guess_too_low(). These 2 cases passed meaning the bug are fixed.
The rest_guess to high() indicates that if secret number is lower, and the hint now prints "Too High" . The test_guess_too_low() indicated that if secret number is higher than guess, the hint printed out is "Too Low".

- Did AI help you design or understand any tests? How?

AI helped me design the rest of the test in test_game_logic.py aside from test_winning_guess(), test_guess_too_high(), and test_guess_too_low(). I told AI the bug I had fixed and asked to help design test cases to test that everything related to the bug had been fixed. The test cases designed were all pretty simple so it was not hard to understand it. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I will use the guessing number game as an example when explaing the concept of Streamlit "reruns" and session state. The way that Streamlit "Reruns" work is that everytime the user interact with the website, streamlit will rerun the whole project over again. With the guessing number game, every time a player presses a button or enter a new guessing number, streamlit will rerun the whole project. With this guessing number game, the number of attempts, the past guesses, and the secret number has to stay the same while the current game is still going on. The session state save the variable while the Streamlit "reruns".

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One habit from this project I want to reuse in future projects is pytest. In the past when I have to do testing, I usually do it manually. Today, I realized pytest is simple to design, and easy to run. Aside from the testing habit, the prompting strategy is a strategy I will also reuse in future labs. In the past, I thought that we could on enter one instruction at a time. Today, with the multi-step instruction in Step 2: Refactor and Fix I learned that users can enter multi-step instruction.

- What is one thing you would do differently next time you work with AI on a coding task? 

I would get used to letting the coding assistant to apply edits directly, after review the code and confirming that there is not problem with the code. I have been used to coding manually with the help of Google in the past. Now, the help of coding assistant really speed up the process on smaller things like pytest or finding where the bugs are if I know what the problem is. I understand that AI coding assistants are not perfect and they can make mistakes, so before letting them apply edits the programmer still has to check if there code is working.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

In the past, when I needed help on a coding part or finding a bug, I rely on print statements or my brain to come up with solutions. At the time, using AI to help coding feels like cheating. With this project, I learned that AI is a tool to help speed up the process, we still have to rely on our brain to work through the problems. I am more comfortable to use AI coding assistant now.
