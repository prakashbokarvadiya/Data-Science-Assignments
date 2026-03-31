# Task 4: Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

def swap_first_two_chars(str1, str2):
    """Swap the first two characters of each string and combine them."""
    if len(str1) < 2 or len(str2) < 2:
        raise ValueError("Both strings must have at least 2 characters")
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + " " + new_str2

# Main program
try:
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    result = swap_first_two_chars(s1, s2)
    print(f"Result: '{result}'")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
pairs = [("abc", "xyz"), ("Hello", "World"), ("Python", "Coding")]
for a, b in pairs:
    print(f"str1='{a}', str2='{b}' => '{swap_first_two_chars(a, b)}'")
