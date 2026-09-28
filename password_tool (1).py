"""
Password Strength Checker + Generator
--------------------------------------
Checks how strong a password is, and can generate a strong one for you.
Concepts used: strings, loops, functions, if/elif, the random module.
"""

import random
import string

COMMON_PASSWORDS = ["password", "123456", "qwerty", "abc123", "letmein", "admin"]


# Check the strength of a password and return a score + list of tips
def check_password(password):
    score = 0
    tips = []

    # Rule 1: Length
    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")

    # Rule 2: Has a lowercase letter
    has_lower = False
    for ch in password:
        if ch.islower():
            has_lower = True
    if has_lower:
        score += 1
    else:
        tips.append("Add at least one lowercase letter.")

    # Rule 3: Has an uppercase letter
    has_upper = False
    for ch in password:
        if ch.isupper():
            has_upper = True
    if has_upper:
        score += 1
    else:
        tips.append("Add at least one uppercase letter.")

    # Rule 4: Has a number
    has_digit = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
    if has_digit:
        score += 1
    else:
        tips.append("Add at least one number.")

    # Rule 5: Has a symbol
    symbols = "!@#$%^&*()_+-=[]{}"
    has_symbol = False
    for ch in password:
        if ch in symbols:
            has_symbol = True
    if has_symbol:
        score += 1
    else:
        tips.append("Add at least one symbol (like ! @ # $).")

    # Rule 6: Not a common password
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        tips = ["This password is too common. Choose something unique."]

    return score, tips


# Turn the score (0 to 5) into a simple label
def score_label(score):
    if score <= 1:
        return "Very Weak"
    elif score == 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"


# Generate a random strong password of a given length
def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"

    # Guarantee at least one of each type
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest randomly from all characters combined
    all_chars = lower + upper + digits + symbols
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    # Shuffle so the guaranteed characters aren't always at the start
    random.shuffle(password_chars)
    return "".join(password_chars)


# Menu option: check a password typed by the user
def check_menu():
    password = input("Enter a password to check: ")
    score, tips = check_password(password)

    print(f"\nStrength: {score_label(score)}  ({score}/5)")
    if tips:
        print("Tips to improve:")
        for tip in tips:
            print(" -", tip)
    else:
        print("Great password!")
    print()


# Menu option: generate a new password
def generate_menu():
    length = int(input("How long should the password be? (min 6): "))
    if length < 6:
        length = 6

    new_password = generate_password(length)
    score, tips = check_password(new_password)
    print(f"\nGenerated password: {new_password}")
    print(f"Strength: {score_label(score)}  ({score}/5)\n")


# Main menu loop
def main():
    while True:
        print("===== PASSWORD TOOL =====")
        print("1. Check a password")
        print("2. Generate a strong password")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            check_menu()
        elif choice == "2":
            generate_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
