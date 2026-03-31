# Task 18: Python Program to Find Factorial of Number Using Recursion

def factorial(n):
    """Find factorial of a number using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Main program
try:
    n = int(input("Enter a number to find its factorial: "))
    result = factorial(n)
    print(f"Factorial of {n} = {result}")
except ValueError as e:
    print(f"Error: {e}")
except RecursionError:
    print("Error: Number is too large for recursion")

# Examples
print("\n--- Examples ---")
for num in [0, 1, 5, 7, 10]:
    print(f"factorial({num}) = {factorial(num)}")
