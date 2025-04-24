import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define the character sets to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all character sets
    all_chars = lowercase + uppercase + numbers + special_chars
    
    if not all_chars:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    # Get user input
    length = int(input("Enter the desired password length (minimum 6): "))
    if length < 6:
        print("Password length should be at least 6.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate and display the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
