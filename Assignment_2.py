# Assignment Two:
# Write a program to handle errors, the program should ask for two numbers using input and then
# divides them. Use an infinite loop to keep asking until a valid input is provided.

# This program asks the user for two numbers and tries to divide them.
# It keeps asking until valid numbers are entered and the division works.
# Errors like invalid input or division by zero are handled with try, except, else, and finally.

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.")
    else:
        print(f"Division successful: {num1} / {num2} = {result}")
        break
    finally:
        print("Attempt completed.\n")