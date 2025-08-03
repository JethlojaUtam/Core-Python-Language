# Initialize a variable to store the sum of even numbers
total_sum = 0

print("Enter even numbers one by one.")
print("If you enter an odd number, it will be ignored.")
print("Enter 0 to stop and calculate the final sum. \n")

# Start an infinite loop to keep asking for input
while True:
    try:
        # Get user input and convert it to an integer
        num = int(input("Enter an even number (or 0 to exit): "))

        # 1. Check if the user wants to exit
        if num == 0:
            break  # Exit the loop

        # 2. Check if the number is ODD
        if num % 2 != 0:
            print(f"⚠️ Oops! {num} is an odd number. It won't be added.")
            continue  # Skip to the next loop iteration

        # 3. If the number is even, add it to the sum
        total_sum += num
        print(f"👍 Added {num}. The current sum is: {total_sum}")

    except ValueError:
        # This runs if the user enters text instead of a number
        print("❌ Invalid input. Please enter a whole number.")

# After the loop finishes, print the final result
print("\n--------------------------------")
print(f"✅ The final sum of all even numbers is: {total_sum}")