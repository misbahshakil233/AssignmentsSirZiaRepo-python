import random

# Word list
word_bank = ["python", "developer", "hangman", "programming", "computer"]

def start_game():
    hidden_word = random.choice(word_bank)
    guessed_letters, remaining_chances = set(), 6

    print("\U0001F3A9 Welcome to Hangman! Try to uncover the hidden word. \U0001F524")

    while remaining_chances > 0:
        print("\nCurrent Word:", " ".join([char if char in guessed_letters else "_" for char in hidden_word]))
        print(f"Attempts left: {remaining_chances}")

        user_input = input("Enter a letter: ").lower()
        if not user_input.isalpha() or len(user_input) != 1 or user_input in guessed_letters:
            print("\u26A0 Invalid or already guessed letter!")
            continue

        guessed_letters.add(user_input)
        if user_input not in hidden_word:
            remaining_chances -= 1
            print("\u274C Wrong guess!")

        if all(char in guessed_letters for char in hidden_word):
            print(f"\U0001F389 Congratulations! You found the word: {hidden_word}")
            return

    print(f"\U0001F480 Game Over! The correct word was: {hidden_word}")

if __name__ == "__main__":
    start_game()
