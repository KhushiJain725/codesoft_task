import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                return length
            else:
                print("Password length must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_character_types():
    char_types = {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "digits": string.digits,
        "special": string.punctuation
    }
    selected_types = []

    for key in char_types:
        while True:
            choice = input(f"Include {key} characters? (yes/no): ").strip().lower()
            if choice in ['yes', 'no']:
                if choice == 'yes':
                    selected_types.append(char_types[key])
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    if not selected_types:
        print("No character types selected. Defaulting to lowercase letters.")
        selected_types.append(string.ascii_lowercase)
    
    return selected_types

def generate_password(length, char_types):
    all_chars = ''.join(char_types)
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = get_password_length()
    char_types = get_character_types()
    password = generate_password(length, char_types)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
