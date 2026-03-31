# Task 20: Mini Project - Password Generator
# Generate a strong password from user input words,
# including numbers, special characters and capital letters.
# Includes a User class to store user details.

import random
import string
import re

# ─────────────────────────────────────────────
# User Class
# ─────────────────────────────────────────────
class User:
    """Stores user details: user_id, name, and password."""

    _id_counter = 1  # Auto-increment user ID

    def __init__(self, name, password):
        if not name or not name.strip():
            raise ValueError("User name cannot be empty")
        self.user_id = User._id_counter
        User._id_counter += 1
        self.name = name.strip()
        self.password = password

    def display(self):
        """Display user details (password masked)."""
        masked = self.password[:2] + "*" * (len(self.password) - 4) + self.password[-2:]
        print(f"\n{'='*40}")
        print(f"  User ID  : {self.user_id}")
        print(f"  Name     : {self.name}")
        print(f"  Password : {masked}")
        print(f"{'='*40}")

    def __str__(self):
        return f"User(id={self.user_id}, name='{self.name}')"


# ─────────────────────────────────────────────
# Password Generator
# ─────────────────────────────────────────────
def generate_password(user_input, min_length=8):
    """
    Generate a strong password from user input.
    - Randomly picks words from the input
    - Inserts numbers, special characters, and capital letters
    - Ensures length > 8
    """
    if not user_input or not user_input.strip():
        raise ValueError("User input cannot be empty")

    # Extract words from input
    words = re.findall(r'[a-zA-Z]+', user_input)
    if not words:
        raise ValueError("Please enter at least one word to generate a password")

    # Randomly select 2-4 words
    num_words = min(random.randint(2, 4), len(words))
    selected_words = random.sample(words, num_words)

    # Build base password: mix of word parts with transformations
    base = ""
    for word in selected_words:
        # Randomly capitalize some letters
        transformed = ''.join(
            ch.upper() if random.random() > 0.5 else ch.lower()
            for ch in word
        )
        base += transformed

    # Add random digits
    digits = ''.join(random.choices(string.digits, k=random.randint(2, 4)))

    # Add special characters
    specials = ''.join(random.choices("!@#$%^&*", k=random.randint(2, 3)))

    # Combine all parts and shuffle
    all_chars = list(base + digits + specials)
    random.shuffle(all_chars)
    password = ''.join(all_chars)

    # Ensure minimum length
    while len(password) <= min_length:
        password += random.choice(string.ascii_letters + string.digits + "!@#$%")

    return password


def validate_password_strength(password):
    """Check if password meets strength requirements."""
    checks = {
        "Length > 8"       : len(password) > 8,
        "Has uppercase"    : any(c.isupper() for c in password),
        "Has lowercase"    : any(c.islower() for c in password),
        "Has digit"        : any(c.isdigit() for c in password),
        "Has special char" : any(c in "!@#$%^&*" for c in password),
    }
    return checks


# ─────────────────────────────────────────────
# Main Program
# ─────────────────────────────────────────────
def main():
    print("=" * 50)
    print("      STRONG PASSWORD GENERATOR")
    print("=" * 50)

    try:
        # Get user details
        name = input("\nEnter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty")

        user_input = input(
            "Enter some words/phrase (password will be generated from these): "
        ).strip()

        # Generate password
        password = generate_password(user_input)

        # Validate strength
        checks = validate_password_strength(password)

        print(f"\n✅ Generated Password: {password}")
        print("\nPassword Strength Check:")
        for check, passed in checks.items():
            status = "✔" if passed else "✘"
            print(f"  [{status}] {check}")

        # Create User object
        user = User(name, password)
        print("\nUser Details Saved:")
        user.display()

    except ValueError as ve:
        print(f"\n[ValueError] {ve}")
    except Exception as ex:
        print(f"\n[Error] {ex}")


# ─────────────────────────────────────────────
# Demo / Example run
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("\n--- Running Demo (bypassing input) ---")
    sample_input = "sunshine ocean mountain breeze"
    sample_name  = "Alice"

    try:
        pwd = generate_password(sample_input)
        checks = validate_password_strength(pwd)
        print(f"Input    : '{sample_input}'")
        print(f"Password : {pwd}")
        print("Strength :", {k: ("✔" if v else "✘") for k, v in checks.items()})

        user = User(sample_name, pwd)
        user.display()

        # Second user example
        pwd2 = generate_password("river valley forest cloud")
        user2 = User("Bob", pwd2)
        print(f"\nSecond user created: {user2}")

    except Exception as e:
        print(f"Demo Error: {e}")
