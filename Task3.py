import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Define the possible character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Start with the lowercase letters as a default
    all_characters = lowercase_letters

    # Add character sets based on user preferences
    if use_uppercase:
        all_characters += uppercase_letters
    if use_numbers:
        all_characters += digits
    if use_symbols:
        all_characters += symbols

    # Randomly select characters to form the password
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    print("Random Password Generator")

    # Get user input for password criteria
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length < 4:
                print("Password length should be at least 4. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the length.")

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)

    # Display the generated password
    print("\nGenerated Password: ", password)

if __name__ == "__main__":
    main()
