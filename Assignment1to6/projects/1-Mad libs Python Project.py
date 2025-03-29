def adventure_story():
    """Generates a fun adventure story based on user input."""
    
    # Taking inputs for the story
    hero = input("Enter the name of the main character: ")
    city = input("Enter a city or place: ")
    pet = input("Enter an animal: ")
    activity = input(f"What was the {pet} doing? ")
    snack = input("Enter a favorite food item: ")
    response = input(f"How did {hero} react? ")

    # Story Template
    story = f"""
    🌟 A Day to Remember! 🌟

    One bright afternoon, {hero} decided to take a walk through the bustling streets of {city}.
    Everything seemed normal until suddenly, a {pet} appeared out of nowhere!

    But this was no ordinary {pet}—it was {activity} right in the middle of the street!
    Curious, {hero} sat down with a {snack} in hand and watched in amazement.

    Just when {hero} thought things couldn’t get any weirder, the {pet} leaped towards them!
    Shocked, {hero} {response}, making everyone around burst into laughter.

    And that, my friend, is how {hero} became the talk of {city} for days to come! 😂
    """

    # Printing the final story
    print("\n📖 Here is your adventure story:\n")
    print(story)

# Running the function
if __name__ == "__main__":
    adventure_story()
