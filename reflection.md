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
| | After pressing new game, everything should refresh. | 
|50| After pressing submit guess the number should go in history, and allow user to enter next number. |User needs to press submit guess button twice to submit next guess. | None |
 13 | I tried to guess correctly at the last attempt. Results should give me correct. | Only allowed 7 attempts. | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
