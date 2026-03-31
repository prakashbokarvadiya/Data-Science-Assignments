# Task 11: Write a Python program to unzip a list of tuples into individual lists.

def unzip_tuples(list_of_tuples):
    """Unzip a list of tuples into individual lists."""
    if not list_of_tuples:
        raise ValueError("List of tuples cannot be empty")
    return [list(col) for col in zip(*list_of_tuples)]

# Main program
try:
    # Example input as hardcoded for demonstration
    data = [(1, 'a'), (2, 'b'), (3, 'c')]
    result = unzip_tuples(data)
    print(f"Original list of tuples: {data}")
    print(f"Unzipped lists: {result}")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
examples = [
    [(1, 2), (3, 4), (5, 6)],
    [('name', 'Alice'), ('age', 25), ('city', 'NY')],
    [(10, 'x', True), (20, 'y', False)],
]
for tuples in examples:
    unzipped = unzip_tuples(tuples)
    print(f"Input : {tuples}")
    for i, lst in enumerate(unzipped):
        print(f"  List {i+1}: {lst}")
    print()
