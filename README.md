# CodeAlpha Hangman Game

## 📌 Project Overview

This project is a simple text-based Hangman game developed using Python as part of the CodeAlpha Python Programming Internship.

The player attempts to guess a randomly selected word one letter at a time. The player has a maximum of 6 incorrect guesses to find the complete word.

## 🎯 Features

- Randomly selects a word from a predefined list of 5 words.
- Allows the player to guess one letter at a time.
- Reveals correctly guessed letters.
- Tracks incorrect guesses with a maximum limit of 6.
- Prevents the player from guessing the same letter repeatedly.
- Validates user input to allow only one alphabetic character.
- Displays the player's guessed letters and current game status.
- Displays a win message when the word is successfully guessed.
- Displays a game-over message when the player reaches 6 incorrect guesses.

## 🛠️ Technologies Used

- Python
- `random` module

## 🧠 Python Concepts Used

- `random.choice()`
- `while` loop
- `if-else` statements
- Strings
- Lists
- `for` loop
- User input and output
- String methods
- List indexing

## 🎮 How the Game Works

1. The program displays the Hangman game title.
2. The player enters their name.
3. The program randomly selects one word from the predefined word list.
4. The selected word is hidden using underscores.
5. The player enters one letter at a time.
6. If the letter exists in the secret word, its position is revealed.
7. If the letter is incorrect, the incorrect guess counter increases.
8. The player can make a maximum of 6 incorrect guesses.
9. The game ends when:
   - The player successfully guesses the complete word, or
   - The player reaches 6 incorrect guesses.

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the following command:

```bash
python hangman.py
```

📁 Project Structure
```text
Hangman-Game/
│
├── hangman.py
└── README.md
```
