# Task 19: Write a Python function that takes a list and returns a new list
# with unique elements of the first list.

def get_unique_elements(lst):
    """Return a new list with only the unique elements, preserving order."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
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
    result = get_unique_elements(nums)
    print(f"Original List : {nums}")
    print(f"Unique List   : {result}")
except TypeError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
test_lists = [
    [1, 2, 3, 3, 4, 4, 5],
    [10, 20, 10, 30, 20, 40],
    ['a', 'b', 'a', 'c', 'b'],
    [1, 1, 1, 1],
]
for lst in test_lists:
    print(f"Input : {lst}")
    print(f"Output: {get_unique_elements(lst)}")
    print()
