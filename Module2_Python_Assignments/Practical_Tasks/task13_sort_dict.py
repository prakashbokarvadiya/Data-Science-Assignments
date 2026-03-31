# Task 13: Write a Python program to sort a dictionary (ascending/descending) by value.

def sort_dict_by_value(d, descending=False):
    """Sort a dictionary by its values in ascending or descending order."""
    if not d:
        raise ValueError("Dictionary cannot be empty")
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=descending))

# Main program
try:
    d = {'banana': 3, 'apple': 1, 'cherry': 5, 'date': 2, 'elderberry': 4}
    print(f"Original dictionary: {d}")
    print(f"Sorted Ascending  : {sort_dict_by_value(d)}")
    print(f"Sorted Descending : {sort_dict_by_value(d, descending=True)}")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
sample = {'math': 85, 'english': 92, 'science': 78, 'history': 88}
print(f"Dictionary: {sample}")
print(f"Ascending : {sort_dict_by_value(sample)}")
print(f"Descending: {sort_dict_by_value(sample, descending=True)}")
