import argparse
import sys
import time
from random import randint as rint
from random import shuffle

# Constants for password characters
SPECIAL_CHARACTERS = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`"
UPPERCASE_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
NUMERIC_CHARACTERS = "0123456789"

def generate_password(length, use_special, use_uppercase, use_lowercase, use_numeric, verbose=False):
    """Generate a password of the specified length."""
    password = ""

    # List of character sets based on user preferences
    character_sets = []
    if use_special:
        character_sets.append(SPECIAL_CHARACTERS)
    if use_uppercase:
        character_sets.append(UPPERCASE_CHARACTERS)
    if use_lowercase:
        character_sets.append(LOWERCASE_CHARACTERS)
    if use_numeric:
        character_sets.append(NUMERIC_CHARACTERS)

    # Check if at least one character set is selected
    if not character_sets:
        print("Error: Please select at least one character set.")
        return ""

    if verbose:
        print("Generating password...", flush=True)

    # Select characters from the chosen character set one by one
    for _ in range(length):
        char_set = character_sets[rint(0, len(character_sets) - 1)]
        password += char_set[rint(0, len(char_set) - 1)]

        if verbose:
            sys.stdout.write(password)
            sys.stdout.flush()
            time.sleep(0.05)
            sys.stdout.write("\r")


    # Shuffle the password to ensure randomness
    password_list = list(password)
    if verbose:
        print("\n\nShuffling...")
    shuffle(password_list)
    return ''.join(password_list)

def main():
    """Main function to execute the program."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, help="Length of the password")
    parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
    parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
    parser.add_argument("-l", "--lowercase", action="store_true", help="Include lowercase letters")
    parser.add_argument("-n", "--numeric", action="store_true", help="Include numeric characters")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show verbose output")
    args = parser.parse_args()

    # Generate password
    if(args.length < 0 or args.length > 200):
        print("Password Length should be between 0-200.")
        return
    password = generate_password(args.length, args.special, args.uppercase, args.lowercase, args.numeric, args.verbose)
    if password:
        print("Generated password:", password)

if __name__ == '__main__':
    main()
