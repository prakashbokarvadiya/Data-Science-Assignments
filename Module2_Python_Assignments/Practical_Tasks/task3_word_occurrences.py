# Task 3: Write a Python program to count the occurrences of each word in a given sentence.

def count_word_occurrences(sentence):
    """Count occurrences of each word in a sentence."""
    if not sentence.strip():
        raise ValueError("Sentence cannot be empty")
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Main program
try:
    sentence = input("Enter a sentence: ")
    word_count = count_word_occurrences(sentence)
    print("\nWord Occurrences:")
    for word, count in sorted(word_count.items()):
        print(f"  '{word}' : {count}")
except ValueError as e:
    print(f"Error: {e}")

# Examples
print("\n--- Examples ---")
test_sentence = "to be or not to be that is the question to be"
result = count_word_occurrences(test_sentence)
print(f"Sentence: '{test_sentence}'")
print("Word Count:", result)
