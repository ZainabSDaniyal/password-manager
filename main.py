import os

if not os.path.exists("passwords.txt"):
    open("passwords.txt", "w").close()

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(site, password):
    with open("passwords.txt", "a") as file:   # FIXED — now correct filename
        file.write(f"{site} : {hash_password(password)}\n")
    print("Password stored successfully!")

def view_passwords():
    with open("passwords.txt", "r") as file:
        content = file.read().strip()
        if not content:
            print("No passwords stored yet.")
        else:
            print(content)


print("PASSWORD MANAGER")
print("1. Save new password")
print("2. View saved passwords")

choice = input("Enter option number: ")

if choice == "1":
    site = input("Enter site/app name: ")
    password = input("Enter password: ")
    save_password(site, password)

elif choice == "2":
    view_passwords()

else:
    print("Invalid choice")
