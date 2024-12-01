import secrets
import string
import os

from cryptography.fernet import Fernet
import os
import sys

def password_generator():
        numCharacters = input("Enter the number of characters: ")
        if numCharacters.isdigit():
            numCharacters = int(numCharacters)
            if numCharacters >= 12:
                alphabet = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(secrets.choice(alphabet) for i in range(int(numCharacters)))

                print("Here is password: " + password)

                file = open("password.txt", "w")
                file.write(password)

                if os.path.exists("password.txt"):
                    print("Password file has been created!\n_____________________________________")
                else:
                    print("There was an error.")
            else:
                print("Number is too small for a secure password.")
        else:
            print("Enter a valid number.")

print("Welcome to Password Generator Program!")
while True:
    numChoice = input("1. Create a new password \n2. Quit\n___________________________\n")
    if numChoice == "1":
        password_generator()
    if numChoice == "2":
        exit()

#password: >Sr%5-ItA^*Vb>]MtD;+&]lz#