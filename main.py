import os
import hashlib
import getpass  

MASTER_FILE = "master.txt"

if not os.path.exists(MASTER_FILE):
    print("Welcome! Let's set up your master password.")
    while True:
        master_pw = getpass.getpass("Enter new master password: ")
        confirm_pw = getpass.getpass("Confirm master password: ")
        if master_pw == confirm_pw:
            hashed_master = hashlib.sha256(master_pw.encode()).hexdigest()
            with open(MASTER_FILE, "w") as f:
                f.write(hashed_master)
            print("Master password set successfully!\n")
            break
        else:
            print("Passwords do not match. Try again.\n")

else:
    hashed_master = open(MASTER_FILE, "r").read().strip()
    for attempt in range(3):
        entered_pw = getpass.getpass("Enter master password: ")
        if hashlib.sha256(entered_pw.encode()).hexdigest() == hashed_master:
            print("Access granted!\n")
            break
        else:
            print("Incorrect password.")
    else:
        print("Too many failed attempts. Exiting...")
        exit()

PASSWORD_FILE = "password.txt"

if not os.path.exists(PASSWORD_FILE):
    open(PASSWORD_FILE, "w").close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(site, password):
    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{site} : {hash_password(password)}\n")
    print("Password stored successfully!\n")

def view_passwords():
    with open(PASSWORD_FILE, "r") as file:
        content = file.read().strip()
        if not content:
            print("No passwords stored yet.\n")
        else:
            print(content + "\n")

print("PASSWORD MANAGER")
print("1. Save new password")
print("2. View saved passwords")

choice = input("Enter option number: ")

if choice == "1":
    site = input("Enter site/app name: ")
    password = getpass.getpass("Enter password to save: ")
    save_password(site, password)
elif choice == "2":
    view_passwords()
else:
    print("Invalid choice\n")
