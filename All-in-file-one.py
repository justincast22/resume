import secrets
import string
import os
from cryptography.fernet import Fernet
import sys

# Helper function to get or create a secure key using environment variables
def get_or_create_key():
    key = os.getenv("FERNET_KEY")
    if not key:
        # Generate a new key
        key = Fernet.generate_key().decode()  # Decode to string for environment variable
        print("Generated a new encryption key.")

        # Automatically save the key to a file for reuse
        with open(".env", "w") as env_file:
            env_file.write(f"FERNET_KEY={key}\n")
        print("Key saved to '.env'. Please reload your environment or restart the script.")

        # Load the key into the current environment automatically
        os.environ["FERNET_KEY"] = key
        print("Key loaded into the current session.")
    return key.encode()

# Function to create a new password and save it to a file
def askUserInfo():
    userWebsite = input("Website: ")
    userEmail = input("Email: ")

    numCharacters = input("Enter the number of characters: ")
    if numCharacters.isdigit() and int(numCharacters) >= 12:
        numCharacters = int(numCharacters)
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(numCharacters))
        print("Here is your password: " + password)

        # Save credentials to file
        with open("credentials.txt", "a") as file:
            file.write("Website: " + userWebsite + "\n")
            file.write("Email: " + userEmail + "\n")
            file.write("Password: " + password + "\n")
            file.write("---------------------------\n")

        print("Credentials saved to 'credentials.txt'.\n")
    else:
        print("Invalid input. Please enter a number greater than or equal to 12.")

# Function to encrypt the file
def encrypt():
    key = get_or_create_key()
    filename = input("Enter the file name to encrypt (e.g., 'credentials.txt'): ")
    if os.path.exists(filename):
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
        print(f"File '{filename}' encrypted successfully.")
    else:
        print(f"File '{filename}' does not exist.")

# Function to decrypt the file (overwrites the same file)
def decrypt():
    key = get_or_create_key()
    filename = input("Enter the file name to decrypt: ")
    if os.path.exists(filename):
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        print(f"File '{filename}' decrypted successfully.")
    else:
        print(f"File '{filename}' does not exist.")

# Main program
print("Welcome!")
while True:
    numChoice = input(
        "1. Create a new password\n2. Encrypt\n3. Decrypt\n4. Quit\n___________________________\n"
    )
    if numChoice == "1":
        askUserInfo()
    elif numChoice == "2":
        encrypt()
    elif numChoice == "3":
        decrypt()
    elif numChoice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select an option from 1 to 4.")
