
import random


# List of words used in the game
WORDS = [
    "PYTHON", "COMPUTER", "PROGRAM", "KEYBOARD",
    "INTERNET", "STUDENT", "SCIENCE", "FUNCTION",
    "DEVELOPER", "VARIABLE", "DATABASE", "SOFTWARE",
    "NETWORK", "HANGMAN", "CODING", "GORITHM",
    "TECHNOLOGY", "APPLICATION", "ENGINEERING",
    "ARTIFICIAL", "INTELLIGENCE", "ALGORITHM",
    "CLOUD", "SECURITY", "PROCESSOR", "MEMORY"
]

MAX_ATTEMPTS = 6


# ASCII gallows stages for each incorrect guess
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden."""
    masked_word = ""

    for letter in word:
        if letter in guessed_letters:
            masked_word += letter + " "
        else:
            masked_word += "_ "

    return masked_word.strip()


def display_game_status(word, guessed_letters,
                        incorrect_guesses):
    """Display the gallows and current game progress."""
    mistakes = len(incorrect_guesses)

    print("\n" + HANGMAN_STAGES[mistakes])
    print("Word:", display_word(word, guessed_letters))
    print("Guessed letters:",
          " ".join(sorted(guessed_letters | incorrect_guesses))
          if guessed_letters or incorrect_guesses else "None")
    print("Incorrect guesses:",
          " ".join(sorted(incorrect_guesses))
          if incorrect_guesses else "None")
    print("Attempts remaining:", MAX_ATTEMPTS - mistakes)


def play_game():
    """Run one round of Hangman."""
    word = random.choice(WORDS)

    guessed_letters = set()
    incorrect_guesses = set()

    print("\n" + "=" * 35)
    print("       HANGMAN WORD GAME")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print("You have 6 incorrect attempts.")

    while True:
        display_game_status(
            word, guessed_letters, incorrect_guesses
        )

        # Check whether the player has guessed the word
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 35)
            print("          YOU WON!")
            print("=" * 35)
            print("Congratulations! The word was:", word)
            print("You guessed it successfully!")
            break

        # Check whether all attempts are used
        if len(incorrect_guesses) == MAX_ATTEMPTS:
            print("\n" + "=" * 35)
            print("          GAME OVER")
            print("=" * 35)
            print("The correct word was:", word)
            print("Better luck next time!")
            break

        guess = input("\nEnter a letter: ").strip().upper()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter one alphabet letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter!")
            print("No attempt has been deducted.")
            continue

        # Check whether the letter is in the word
        if guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            incorrect_guesses.add(guess)
            print("Wrong guess!")


def main():
    """Start the game and allow replay."""
    while True:
        play_game()

        play_again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if play_again not in ("yes", "y"):
            print("\nThanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()
