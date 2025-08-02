# ----------------------------------------------------------------
# Program 1: Simple 'if' statement
# This program checks if a user-entered number is positive.
# ----------------------------------------------------------------
print("--- Program 1: Simple 'if' Statement ---")
number_one = int(input("Enter a number: "))

if number_one > 0:
    print(f"The number {number_one} is positive.\n")

# ----------------------------------------------------------------
# Program 2: 'if-else' statement
# This program checks if a number is even or odd.
# ----------------------------------------------------------------
print("--- Program 2: 'if-else' Statement ---")
number_two = int(input("Enter another number: "))

if number_two % 2 == 0:
    print(f"The number {number_two} is even.\n")
else:
    print(f"The number {number_two} is odd.\n")

# ----------------------------------------------------------------
# Program 3: 'if-elif-else' ladder
# This program assigns a grade based on a score.
# ----------------------------------------------------------------
print("--- Program 3: 'if-elif-else' Ladder ---")
score = int(input("Enter a score (0-100): "))
grade = ''

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"A score of {score} gets a grade of '{grade}'.\n")

# ----------------------------------------------------------------
# Program 4: 'for' loop
# This program prints numbers from 1 to 5 and calculates their sum.
# ----------------------------------------------------------------
print("--- Program 4: 'for' Loop ---")
total_sum = 0
print("Calculating the sum of numbers from 1 to 5:")
for i in range(1, 6): # The range(1, 6) generates numbers 1, 2, 3, 4, 5
    print(f"Adding {i}")
    total_sum += i

print(f"The sum of numbers from 1 to 5 is: {total_sum}\n")

# ----------------------------------------------------------------
# Program 5: 'while' loop
# A simple number guessing game.
# ----------------------------------------------------------------
print("--- Program 5: 'while' Loop ---")
secret_number = 7
guess = 0

print("I'm thinking of a number between 1 and 10.")
while guess != secret_number:
    try:
        guess = int(input("What's your guess? "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"You got it! The secret number was {secret_number}.\n")
