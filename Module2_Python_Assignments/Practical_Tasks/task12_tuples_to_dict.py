# Task 12: Write a Python program to convert a list of tuples into a dictionary.

def tuples_to_dict(list_of_tuples):
    """Convert a list of (key, value) tuples into a dictionary."""
    if not list_of_tuples:
        raise ValueError("List cannot be empty")
    return dict(list_of_tuples)

# Main program
try:
    data = [('name', 'Alice'), ('age', 25), ('city', 'Mumbai')]
    result = tuples_to_dict(data)
    print(f"List of tuples : {data}")
    print(f"Dictionary     : {result}")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
examples = [
    [(1, 'one'), (2, 'two'), (3, 'three')],
    [('a', 1), ('b', 2), ('c', 3)],
    [('x', 10), ('y', 20), ('z', 30)],
]
for t in examples:
    print(f"Tuples: {t} => Dict: {tuples_to_dict(t)}")
