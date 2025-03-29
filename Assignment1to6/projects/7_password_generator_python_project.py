import random
import string

def generate_password(length):
    """Generates a random password with letters, numbers, and symbols."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

try:
    num_passwords = int(input("How many passwords do you want to generate? "))
    length = int(input("Enter password length: "))

    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        print(generate_password(length))

except ValueError:
    print("Invalid input! Please enter a number.")
