import time

def countdown(seconds):
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        print(f"{minutes:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter countdown time in seconds: "))
        countdown(user_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
