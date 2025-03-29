import random

def number_guessing_game():
    """A fun number guessing game with 5 rounds."""
    print("🎯 Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.\n")

    for round_num in range(1, 6):  # Runs exactly 5 rounds
        target = random.randint(1, 100)
        print(f"\n🔵 Round {round_num}: Can you guess the number?")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                
                if guess < 1 or guess > 100:
                    print("❌ Out of range! Guess a number between 1 and 100.")
                elif guess < target:
                    print("⬆️ Too low! Try again.")
                elif guess > target:
                    print("⬇️ Too high! Try again.")
                else:
                    print(f"🎉 Correct! The number was {target}.")
                    break
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

    print("\n🏆 Game Over! Thanks for playing!")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
