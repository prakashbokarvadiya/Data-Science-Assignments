# Task 2: Write a Python program to count occurrences of a substring in a string.

def count_substring(main_string, substring):
    """Count occurrences of a substring in a given string."""
    if not substring:
        raise ValueError("Substring cannot be empty")
    return main_string.count(substring)

# Main program
try:
    main_str = input("Enter the main string: ")
    sub_str = input("Enter the substring to count: ")
    count = count_substring(main_str, sub_str)
    print(f"The substring '{sub_str}' appears {count} time(s) in the given string.")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
examples = [
    ("hello world hello", "hello"),
    ("aaaa", "aa"),
    ("Python is great. Python is fun.", "Python"),
]
for s, sub in examples:
    print(f"String: '{s}' | Substring: '{sub}' | Count: {count_substring(s, sub)}")
