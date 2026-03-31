# Task 9: Write a Python program to find the second smallest number in a list.

def second_smallest(lst):
    """Find the second smallest unique number in a list."""
    if len(lst) < 2:
        raise ValueError("List must have at least 2 elements")
    unique_sorted = sorted(set(lst))
    if len(unique_sorted) < 2:
        raise ValueError("List must have at least 2 distinct values")
    return unique_sorted[1]

# Main program
try:
    nums = list(map(int, input("Enter list elements (space separated): ").split()))
    result = second_smallest(nums)
    print(f"Second smallest number in {nums} = {result}")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
lists = [
    [10, 20, 4, 45, 99],
    [1, 1, 2, 3],
    [5, 3, 8, 1, 2],
]
for lst in lists:
    print(f"List: {lst} => Second smallest: {second_smallest(lst)}")
