# Assignment find the factorial of a number (five)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calculate 5!
fact = factorial(5)
print(f"The factorial of 5 is: {fact}")