import random

def computer_guesses():
    print("🎯 Think of a number between 1 and 100, and I'll try to guess it!")

    low, high = 1, 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2  # Smart guessing
        attempts += 1

        print(f"Is your number {guess}?")
        user_feedback = input("Enter 'h' for too high, 'l' for too low, or 'c' for correct: ").lower()

        if user_feedback == "h":
            high = guess - 1
        elif user_feedback == "l":
            low = guess + 1
        elif user_feedback == "c":
            print(f"🎉 I guessed your number {guess} in {attempts} tries!")
            return
        else:
            print("⚠️ Please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    computer_guesses()
