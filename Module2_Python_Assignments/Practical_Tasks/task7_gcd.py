# Task 7: Program to find Greatest Common Divisor (GCD) of two numbers.
# GCD of 20 and 28 is 4 | GCD of 98 and 56 is 14

def gcd(a, b):
    """Find GCD using Euclidean algorithm."""
    if a < 0 or b < 0:
        raise ValueError("Numbers must be non-negative")
    while b:
        a, b = b, a % b
    return a

# Main program
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = gcd(num1, num2)
    print(f"GCD of {num1} and {num2} = {result}")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
pairs = [(20, 28), (98, 56), (100, 75), (17, 13)]
for a, b in pairs:
    print(f"GCD({a}, {b}) = {gcd(a, b)}")
