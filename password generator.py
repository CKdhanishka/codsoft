import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return ""

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    # Ensure the password has at least one of each type
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password list
    random.shuffle(password)

    return ''.join(password)

# ---- Main Program ----
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")