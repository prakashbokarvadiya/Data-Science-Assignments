# Task 10: Write a Python program to get unique values from a list.

def get_unique_values(lst):
    """Return unique values from a list preserving order."""
    seen = set()
    unique = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    return unique

# Main program
try:
    nums = list(map(int, input("Enter list elements (space separated): ").split()))
    result = get_unique_values(nums)
    print(f"Original list : {nums}")
    print(f"Unique values : {result}")
except Exception as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
lists = [
    [1, 2, 2, 3, 3, 3, 4],
    [10, 20, 10, 30, 20, 50],
    [5, 5, 5, 5],
]
for lst in lists:
    print(f"Original: {lst} => Unique: {get_unique_values(lst)}")
