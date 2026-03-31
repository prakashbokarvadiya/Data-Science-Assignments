# Task 17: Write a python program using function to find the sum of odd and even series.
# Odd series : 1²/1! + 3²/3! + 5²/5! + ... up to n terms
# Even series: 2²/2! + 4²/4! + 6²/6! + ... up to n terms

import math

def odd_series_sum(n):
    """Calculate sum of odd series: 1²/1! + 3²/3! + 5²/5! + ... up to n terms."""
    total = 0
    for i in range(n):
        num = 2 * i + 1  # 1, 3, 5, ...
        total += (num ** 2) / math.factorial(num)
    return total

def even_series_sum(n):
    """Calculate sum of even series: 2²/2! + 4²/4! + 6²/6! + ... up to n terms."""
    total = 0
    for i in range(1, n + 1):
        num = 2 * i  # 2, 4, 6, ...
        total += (num ** 2) / math.factorial(num)
    return total

# Main program
try:
    n = int(input("Enter number of terms (n): "))
    if n <= 0:
        raise ValueError("n must be positive")

    odd_sum = odd_series_sum(n)
    even_sum = even_series_sum(n)

    print(f"\nFor n = {n} terms:")
    print(f"Odd  Series Sum = {odd_sum:.6f}")
    print(f"Even Series Sum = {even_sum:.6f}")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
for n in [3, 5, 7]:
    print(f"n={n} | Odd Sum = {odd_series_sum(n):.6f} | Even Sum = {even_series_sum(n):.6f}")
