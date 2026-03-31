# Task 15: Given a number n, write a python program to make and print the list
# of Fibonacci series up to n terms.
# Input: n=7 | Output: 0, 1, 1, 2, 3, 5, 8, 13

def fibonacci(n):
    """Generate Fibonacci series of n terms."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    fib = [0, 1]
    for _ in range(n - 1):
        fib.append(fib[-1] + fib[-2])
    return fib[:n + 1]

# Main program
try:
    n = int(input("Enter the value of n: "))
    series = fibonacci(n)
    print(f"First few Fibonacci numbers are: {', '.join(map(str, series))}")
except ValueError as e:
    print(f"Error: {e}")

# Example
print("\n--- Example ---")
n = 7
series = fibonacci(n)
print(f"n = {n}")
print(f"First few Fibonacci numbers are {', '.join(map(str, series))}")
