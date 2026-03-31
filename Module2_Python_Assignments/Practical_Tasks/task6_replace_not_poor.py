# Task 6: Write a Python program to find the first appearance of 'not' and 'poor'
# from a given string. If 'not' follows 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

def replace_not_poor(s):
    """Replace 'not'...'poor' substring with 'good' if 'not' follows 'poor'."""
    not_pos = s.find("not")
    poor_pos = s.find("poor")

    if not_pos != -1 and poor_pos != -1 and poor_pos > not_pos:
        return s[:not_pos] + "good" + s[poor_pos + 4:]
    return s

# Main program
try:
    text = input("Enter a string: ")
    result = replace_not_poor(text)
    print(f"Result: '{result}'")
except Exception as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
test_cases = [
    "This is not a poor solution",
    "The code is not that poor",
    "poor is before not here",
    "Nothing here matches",
]
for t in test_cases:
    print(f"Input : '{t}'")
    print(f"Output: '{replace_not_poor(t)}'")
    print()
