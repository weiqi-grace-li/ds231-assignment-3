# DS231 Assignment 3

## Overview and Objectives
In this assignment, you will build a word-guessing game called *Word Scramble*. The primary goal is to practice writing and calling functions in Python. You will also learn how to break down a complex computational task into smaller, manageable parts by creating helper functions.

## Instructions
1. All your code goes into `word_scramble.py`, the starter file provided in the repository. No need to create any new Python files.
2. Ensure that your program runs without errors. If your code fails to execute, a flat 20% point deduction will be applied, regardless of the nature of the error.
3. For Part 1, correctness is graded based on your functions' return values. To be eligible for partial credit, implement the intermediate variables indicated in ***Function specification*** so that we can identify which parts of your function are working correctly.
4. For Part 2, correctness is graded based on what your program prints to the terminal, as in previous assignments. Make sure your output matches the ***Example output*** exactly.
5. Start early. This assignment involves building a complete interactive game with multiple components. It will likely take more time than previous assignments, so plan accordingly.


## Introduction
By implementing *Word Scramble*, users will play a guessing game against the computer. The program loads a list of words, selects one at random, and scrambles its letters. The user then has a limited number of attempts to guess the original word. We will build the program in two stages: first implementing a set of helper functions, then assembling them into the main game loop.

**Game overview.** The game proceeds as follows:

1. The computer selects a word at random from `words.txt`. All words in this file are in lowercase.
2. The user is given a fixed number of guesses at the start.
3. On each turn, the user enters a guess. The computer then either:
   - rejects the guess as invalid if it does not contain exactly the same letters as the secret word, without penalizing the user, or
   - accepts the guess, decrements the remaining attempts, and reveals which letters were placed correctly (all others are shown as `*`).
4. The game ends when the user guesses the word correctly or runs out of attempts.

***Example playthrough.***

```text
Welcome to Word Scramble!
Scrambled word: acret
You have 5 attempts to guess the original word.

Your guess: !!actor##
Invalid input. Please use only the letters from the secret word.

Your guess: crate
Incorrect. Progress: *ra*e
Attempts left: 4

Your guess: caret
Incorrect. Progress: *****
Attempts left: 3

Your guess: trace
Congratulations! You guessed the word: trace
```

**File setup.** Accept the assignment on GitHub Classroom and clone the repository to your local machine. The repository includes everything you need: `word_scramble.py` and `words.txt`. Once cloned, run `word_scramble.py` to confirm the setup is working. You should see:

```text
Loading word list from file...
10000 words loaded
```


## Part 1. Helper Functions [65 Points]

To keep the main game logic clean and readable, we divide the program into helper functions — smaller, self-contained pieces that each handle one specific task. Six helper functions are needed in total. Three of them (`load_words()`, `choose_word()`, and `scramble_word()`) are already implemented in `word_scramble.py`. Your job is to implement the remaining three.

Here is a summary of all six functions for reference:

- `load_words()` — takes no arguments; reads `words.txt` and returns a list of all valid words in lowercase.
- `choose_word(wordlist)` — takes a word list and returns one word chosen at random.
- `scramble_word(secret_word)` — takes the secret word, scrambles its letters, prints `"Scrambled word: [scrambled version]"`, and returns nothing.
- `input_check(secret_word)` — prompts the user for a guess, validates it, and returns a cleaned version of the first valid guess received.
- `has_player_won(secret_word, user_guess)` — compares the secret word to the user's guess and returns whether they match.
- `get_word_progress(secret_word, user_guess)` — returns a string that reveals correctly placed letters and masks the rest with `*`.

### Task 1.1 — Prompt User for Valid Input [30 Points]

**`input_check(secret_word)`** repeatedly prompts the user for a guess until a valid one is entered, then returns it in cleaned form. The validation process is as follows:

1. Remove all non-letter characters from the input (e.g. `"!!#Word"` → `"Word"`).
2. Convert all remaining letters to lowercase (e.g. `"Word"` → `"word"`).
3. Check whether the cleaned guess uses exactly the same letters as `secret_word`. If it does, return the cleaned guess. If not, print `"Invalid input. Please use only the letters from the secret word."` and prompt the user again.

***Function specification.***
- Input: `secret_word` (str)
- Return: the cleaned, valid guess (str)
- Intermediate variables for partial credit: `guess_cleaned` — a string containing only the letter characters from the raw input [10 pt], all in lowercase [10 pt]

***Function demonstration.***

```text
>>> input_check("word")
Your guess: wordd
Invalid input. Please use only the letters from the secret word.
Your guess: wwoayd
Invalid input. Please use only the letters from the secret word.
Your guess: !!rowd&&
```

Once a valid guess is entered, the function returns the cleaned result (`"rowd"`) without printing anything. The game loop built in Part 2 will use this return value.

***Hint.***
- *Cleaning the input.* Loop through each character in the raw input string. Use `.isalpha()` to check whether a character is a letter — for example, `"!".isalpha()` returns `False` and `"S".isalpha()` returns `True`. If the character is a letter, convert it to lowercase with `.lower()` and add it to a new string; otherwise, skip it.
- *Checking valid letters.* Use `sorted()` on both the cleaned guess and `secret_word`, then compare the two results with `==`. `sorted()` returns the characters of a string in alphabetical order, so two strings with the same letters always produce the same sorted list regardless of arrangement. For example, both `sorted("crate")` and `sorted("trace")` produce `['a', 'c', 'e', 'r', 't']`.

### Task 1.2 — Check for Correct Guess [5 Points]

**`has_player_won(secret_word, user_guess)`** checks whether the user's guess matches the secret word exactly.

***Function specification.***
- Input: `secret_word` (str), `user_guess` (str)
- Return: `True` if the guess is correct, `False` otherwise (bool)

***Function demonstration.***

```text
>>> has_player_won("apple", "apple")
True
>>> has_player_won("apple", "paple")
False
```

### Task 1.3 — Reveal Correctly Placed Letters [30 Points]

**`get_word_progress(secret_word, user_guess)`** gives the user positional feedback after an incorrect guess. The logic is as follows:

1. Compare `secret_word` and `user_guess` character by character, position by position.
2. Where the letters match at a position, keep that letter in the result.
3. Where they do not match, place a `*` in the result.

***Function specification.***
- Input: `secret_word` (str), `user_guess` (str)
- Return: a string of the same length as `secret_word`, with correctly placed letters shown and all others replaced by `*` (str)
- No intermediate variables required. Partial credit will be awarded based on the correctness of your return value.

***Function demonstration.***

```text
>>> get_word_progress("elephant", "elepanht")
'elep***t'
>>> get_word_progress("table", "batle")
'*a*le'
```

***Hint.*** Loop through the indices of `secret_word`. At each index, compare `secret_word[i]` and `user_guess[i]`, and build the result string one character at a time.


## Part 2. The Game [35 Points]

With the helper functions in place, you will now implement the main game logic inside `word_scramble()`. This function runs the full interactive game, making use of `input_check()`, `has_player_won()`, and `get_word_progress()` from Part 1.

### Task 2.1 — Game Setup [10 Points]

Before the game loop begins, the function loads `words.txt` into a list of words, `word_list`. Continue setting up the game as follows:

1. Select a random word using `choose_word()` and display its scrambled version using `scramble_word()`.
2. Print a welcome message and inform the user how many attempts they have.

***Example output.***

```text
Welcome to Word Scramble!
Scrambled word: acret
You have 5 attempts to guess the original word.
```

***Hint.*** Even though `load_words()`, `choose_word()`, and `scramble_word()` were not implemented by you, their descriptions at the beginning of Part 1 tell you exactly what inputs they take and what they return — that is all you need to use them correctly.

### Task 2.2 — Main Interaction Loop [25 Points]

Implement the main game loop inside `word_scramble(secret_word)` as follows:

1. While attempts remain, call `input_check(secret_word)` to get a valid guess from the user.
2. If `has_player_won()` returns `True`, print a congratulatory message and end the game.
3. Otherwise, decrement attempts by 1, display progress using `get_word_progress()`, and continue to the next turn.
4. If attempts reach 0 without a correct guess, print `"Sorry, you ran out of guesses. The word was [secret_word]."`

***Example output.***

`secret_word = "crane"`, `scrambled = "necra"`

```text
Welcome to Word Scramble!
Scrambled word: necra
You have 5 attempts to guess the original word.

Your guess: caner
Incorrect. Progress: c****
Attempts left: 4

Your guess: nacre
Incorrect. Progress: ****e
Attempts left: 3

Your guess: crane
Congratulations! You guessed the word: crane
```

***Hints.***
- Use a `while` loop to control the game turns.
- Use `print()` with no arguments to print an empty line between turns.
