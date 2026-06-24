# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - The hints didn't properly correspond to the correct answer. For example, when the secret number was 5, the guesser would say to guess higher tna 93 but lower than 2.
  - After a game is completed, the new game button doesn't work. 
  - If you unclick then reclick show hint, the hints do not come back

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 2| "Go Higher"|"Go Lower |None |
| Guess of 93| "Go Lower| "Go Higher| None|
| Guess of -5| "Out of Range | "Go Lower" | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude AI
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One AI suggesting was changing the results of the pytests, as the guess_check returns a tuple and the tests were checking against only one value. It made the helpful suggesting separating the parts of the tuple and comparing our expectation on the first value that is.returned from guess_check
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One example of an AI suggestion that appeared to be misleading was when it wanted to check if numeric_guess is not None, when checking if a number was out of range in the check_guess method. It then explained that it didn't matter if the portion of the if statement was included or not (as long as the range was checked).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I used the pytests in a way that test multiple edge cases within the bug I fixed.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
One test I ran checked if the guess was out of the 1 to 100 range. It showed that my code was correct because it passed not only for when it was less than the guess range but also higher than the guess range.
- Did AI help you design or understand any tests? How?
Yes, AI helped me design my tests, by considering the types of cases that I may encounter when functions are ran.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
A rerun wipes a way "global" variables (e.g secret number, score, number of attempts left), while a session state holds those values.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to continue to ask questions on wierd logic, such as tries and exceptions and understand when/why the work or don't. 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I also want to make sure that I prompt for all potential test cases, both regular and edge cases.
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I would do differently is begin with an assessment of what is expected of the code, going through an explanation of each function's purpose, as to better understand where bugs may be.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project helped me realized that using AI to code doesn't need to look like "Code this whole project". When done right, it looks like a collaborative effort, where the code is the leader and decision maker, not AI.
