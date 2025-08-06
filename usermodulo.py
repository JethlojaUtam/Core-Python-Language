# Get the first number from the user
num1_str = input("Enter the first number: ")

# Get the second number from the user
num2_str = input("Enter the second number: ")

# Convert the input strings to integers
num1 = int(num1_str)
num2 = int(num2_str)

# Calculate the module
module_result = num1 % num2

# Display the result
print("The modulo of", num1, "and", num2, "is:", module_result)