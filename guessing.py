import random  # Importing the random module to generate a random number

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    while True:  # Keep the game running until the player guesses correctly
        try:
            # Take input from the user
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the attempts each time a guess is made

            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break  # Exit the loop when the correct number is guessed

        except ValueError:
            # Handle invalid inputs (e.g., non-integer inputs)
            print("Please enter a valid integer!")

# Call the game function to start playing
number_guessing_game()
