def joke_bot():
    user_input = input("What do you want? ")  
    if user_input == "Joke":
        print("Here is a joke for you!\nA programmer tells Sophia: get a liter of milk, and if they have eggs, get 12.\nSophia returns with 13 liters of milk. Programmer asks why?\nSophia replies: 'because they had eggs'")
    else:
        print("Sorry, I only tell jokes.")

joke_bot()
