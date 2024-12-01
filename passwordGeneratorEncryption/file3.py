from cryptography.fernet import Fernet
import os
import sys

def decrypt_file(key):
    filename = input("Enter the file name(file.txt): ")
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open("passwordDecrypted.txt", "wb") as file:
        file.write(decrypted_data)

def generate_key():
    """Generate and save the key only if it doesn't exist."""
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
        print("Key generated and saved as 'key.key'.")
    else:
        print("Key already exists.")

def load_key():
    """Load the existing key from the file."""
    return open('key.key', 'rb').read()

print("welcome.")
while True:
    generate_key()
    key = load_key()
    numChoice = input("1.Decrypt file\n2.Exit\n___________________________\n")
    if numChoice == "1":
        decrypt_file(key)
    if numChoice == "2":
        exit()