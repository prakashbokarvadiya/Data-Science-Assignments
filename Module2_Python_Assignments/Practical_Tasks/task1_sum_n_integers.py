# Task 1: Write a Python program to sum of the first n positive integers.

def sum_of_n_integers(n):
    """Calculate the sum of the first n positive integers."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return n * (n + 1) // 2

# Main program
try:
    n = int(input("Enter the value of n: "))
    result = sum_of_n_integers(n)
    print(f"Sum of first {n} positive integers = {result}")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
for n in [5, 10, 100]:
    print(f"Sum of first {n} positive integers = {sum_of_n_integers(n)}")
