# Task 14: Write a Python program to find the highest 3 values in a dictionary.

def top_3_values(d):
    """Return the top 3 highest values from a dictionary."""
    if len(d) < 3:
        raise ValueError("Dictionary must have at least 3 entries")
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:3]

# Main program
try:
    d = {'Alice': 95, 'Bob': 87, 'Charlie': 92, 'Diana': 78, 'Eve': 88}
    top3 = top_3_values(d)
    print("Top 3 values:")
    for rank, (key, val) in enumerate(top3, 1):
        print(f"  {rank}. {key} : {val}")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
sample = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}
print(f"Dictionary : {sample}")
print(f"Top 3      : {top_3_values(sample)}")
