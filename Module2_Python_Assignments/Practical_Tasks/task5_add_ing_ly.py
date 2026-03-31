# Task 5: Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the string already ends with 'ing', add 'ly'.
# If the string length is less than 3, leave it unchanged.

def add_ing_or_ly(word):
    """Add 'ing' or 'ly' based on the rules."""
    if len(word) < 3:
        return word
    elif word.endswith("ing"):
        return word + "ly"
    else:
        return word + "ing"

# Main program
try:
    word = input("Enter a string: ")
    result = add_ing_or_ly(word)
    print(f"Result: '{result}'")
except Exception as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
test_words = ["abc", "string", "sing", "running", "go", "ab"]
for w in test_words:
    print(f"'{w}' => '{add_ing_or_ly(w)}'")
