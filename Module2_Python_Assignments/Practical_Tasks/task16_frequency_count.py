# Task 16: Counting the frequencies in a list using a dictionary in Python.
# Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
# Output: 1:5, 2:4, 3:3, 4:3, 5:2

def count_frequencies(lst):
    """Count frequencies of elements in a list using a dictionary."""
    if not lst:
        raise ValueError("List cannot be empty")
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return dict(sorted(freq.items()))

# Main program
try:
    input_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
    freq = count_frequencies(input_list)
    print(f"Input  : {input_list}")
    print("Output :", ' , '.join(f"{k} : {v}" for k, v in freq.items()))
except ValueError as e:
    print(f"Error: {e}")

# Another example
print("\n--- Another Example ---")
lst2 = ['a', 'b', 'a', 'c', 'b', 'a']
freq2 = count_frequencies(lst2)
print(f"Input  : {lst2}")
print("Output :", ' , '.join(f"{k} : {v}" for k, v in freq2.items()))
