# Initialize a variable to store the sum of odd numbers
total_sum = 0

print("Enter odd numbers one by one.")
print("If you enter an even number, it will be ignored.")
print("Enter 0 to stop and calculate the final sum. \n")

# Start an infinite loop to keep asking for input
while True:
    try:
        # Get user input and convert it to an integer
        num = int(input("Enter an odd number (or 0 to exit): "))

        # 1. Check if the user wants to exit
        if num == 0:
            break  # Exit the loop

        # 2. Check if the number is even
        if num % 2 == 0:
            print(f"⚠️ Oops! {num} is an even number. It won't be added.")
            continue  # Skip to the next loop iteration

        # 3. If the number is odd, add it to the sum
        total_sum += num
        print(f"👍 Added {num}. The current sum is: {total_sum}")

    except ValueError:
        # This runs if the user enters text instead of a number
        print("❌ Invalid input. Please enter a whole number.")

# After the loop finishes, print the final result
print("\n--------------------------------")
print(f"✅ The final sum of all odd numbers is: {total_sum}")