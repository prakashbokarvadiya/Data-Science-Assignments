# Task 8: Write a Python program to check whether a list contains a sublist.

def contains_sublist(main_list, sub_list):
    """Check if sub_list is a contiguous sublist of main_list."""
    if not sub_list:
        return True  # Empty list is always a sublist
    if len(sub_list) > len(main_list):
        return False

    sub_len = len(sub_list)
    for i in range(len(main_list) - sub_len + 1):
        if main_list[i:i + sub_len] == sub_list:
            return True
    return False

# Main program
try:
    main = list(map(int, input("Enter main list elements (space separated): ").split()))
    sub = list(map(int, input("Enter sublist elements (space separated): ").split()))
    result = contains_sublist(main, sub)
    print(f"Is {sub} a sublist of {main}? {result}")
except Exception as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
tests = [
    ([1, 2, 3, 4, 5], [2, 3, 4]),
    ([1, 2, 3, 4, 5], [3, 5]),
    ([10, 20, 30], [10, 20, 30]),
    ([1, 2], [1, 2, 3]),
]
for ml, sl in tests:
    print(f"Main: {ml}, Sublist: {sl} => {contains_sublist(ml, sl)}")
