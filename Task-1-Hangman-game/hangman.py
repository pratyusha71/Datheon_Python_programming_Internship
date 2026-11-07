import random
words = [
    "python",
    "computer",
    "developer",
    "programming",
    "artificial",
    "technology"
]
secret_word = random.choice(words)

guessed_letters = set()

attempts = 6
stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]
print("=================================")
print("       HANGMAN WORD GAME")
print("=================================")

print("\nGuess the hidden word!")
while attempts > 0:

    print(stages[6 - attempts])
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts remaining:", attempts)
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word!")
        break
    guess = input("\nEnter a letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet!")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.add(guess)
    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Incorrect guess!")
else:
    print(stages[6])
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)