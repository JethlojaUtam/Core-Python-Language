import random

def guessing_game():
    """
    A simple number guessing game where the user tries to guess a number
    between 1 and 100.
    """
    # Generate a random integer between 1 and 100.
    # This is the number the user needs to guess.
    secret_number = random.randint(1, 100)
    
    # Initialize the number of guesses the user has made.
    guess_count = 0
    
    # Initialize the user's guess to a value that cannot be correct.
    user_guess = 0

    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("-" * 44)

    # Loop continuously until the user guesses the correct number.
    while user_guess != secret_number:
        try:
            # Prompt the user for their guess and convert it to an integer.
            user_guess_input = input("Enter your guess: ")
            user_guess = int(user_guess_input)
            
            # Increment the guess counter.
            guess_count += 1

            # Compare the user's guess to the secret number and provide feedback.
            if user_guess < secret_number:
                print("Too low! Try a higher number.")
            elif user_guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                # The user guessed correctly.
                print(f"\nCongratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {guess_count} guesses.")
                
        except ValueError:
            # Handle cases where the user enters non-numeric input.
            print("Oops! That's not a valid number. Please enter a number between 1 and 100.")
        
        print() # Add a blank line for better readability.

# --- Main execution block ---
if __name__ == "__main__":
    guessing_game()