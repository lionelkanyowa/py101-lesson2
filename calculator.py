# When writing a program, first write some pseudocode before writing any code:

# Ask the user for the first number
# Ask the user for the second number
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal

# Welcome the user to the program:
print("Welcome to the Calculator!")

# Ask the user for the first number
print("What's the first number?")
number1 = input()
print("What's the second number?")
number2 = input()

# printing the numbers
# print(f'{number1} {number2')

print('What operation would you like to perform?\n(1)Add (2)Subtract (3)Multiply (4)Divide')
operation = input()

# perform if/else statement to perform arithmetic operations based on user request.

if operation == '1': # '1' represents addition
    output = int(number1) + int(number2)
elif operation == '2': # '2' represents subtraction
    output = int(number1) - int(number2)
elif operation == '3': # '3' represents multiplication
    output = int(number1) * int(number2)
elif operation == '4': # '4' represents multiplication
    output = int(number1) / int(number2)

print(f"The result is: {output}")
 


