import random

def main():
    secret = random.randint(1, 99)  
    print("Guess the number between 1 to 99")

    while True: 
        user = int(input("Enter your guess: "))  

        if user < secret:
            print("You guessed too low!")
        elif user > secret:
            print("You guessed too high!")
        else:
            print(f"Congratulations! The number was {secret} 🎉") 
            break  

main()
  