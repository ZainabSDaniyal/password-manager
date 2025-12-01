import os
import hashlib
import getpass

MASTER_FILE = "master.txt"
PASSWORD_FILE = "password.txt"

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

if not os.path.exists(PASSWORD_FILE):
    open(PASSWORD_FILE, "w").close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(platform, username, password):
    with open(PASSWORD_FILE, "a") as file:
        file.write(f"{platform} | {username} | {hash_password(password)}\n")
    print("Password stored successfully!\n")

def view_passwords():
    with open(PASSWORD_FILE, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No passwords stored yet.\n")
            return
        print("\nStored accounts:")
        print("-------------------------------")
        for line in lines:
            platform, username, hashed = line.strip().split(" | ")
            print(f"Platform: {platform}")
            print(f"Username: {username}")
            print(f"Hashed Password: {hashed}")
            print("-------------------------------")

def search_password():
    keyword = input("Enter search keyword: ").lower()
    found = False
    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            if keyword in line.lower():
                platform, username, hashed = line.strip().split(" | ")
                print("-------------------------------")
                print(f"Platform: {platform}")
                print(f"Username: {username}")
                print(f"Hashed Password: {hashed}\n")
                found = True
    if not found:
        print("No matching entries found.\n")

def delete_password():
    search_term = input("Enter platform or username to delete: ").lower()
    updated_lines = []
    deleted = False
    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            if search_term in line.lower():
                print(f"Deleting: {line.strip()}")
                deleted = True
            else:
                updated_lines.append(line)
    with open(PASSWORD_FILE, "w") as file:
        for line in updated_lines:
            file.write(line)
    if deleted:
        print("Entry deleted.\n")
    else:
        print("No matching entry found.\n")

def modify_password():
    search_term = input("Enter platform or username to modify: ").lower()
    updated_lines = []
    modified = False
    with open(PASSWORD_FILE, "r") as file:
        for line in file:
            if search_term in line.lower():
                platform, username, hashed = line.strip().split(" | ")
                print(f"Modifying entry: {line.strip()}")
                new_username = input("Enter new username (leave blank to keep same): ")
                new_password = getpass.getpass("Enter new password (leave blank to keep same): ")
                if new_username:
                    username = new_username
                if new_password:
                    hashed = hash_password(new_password)
                updated_lines.append(f"{platform} | {username} | {hashed}\n")
                modified = True
            else:
                updated_lines.append(line)
    with open(PASSWORD_FILE, "w") as file:
        for line in updated_lines:
            file.write(line)
    if modified:
        print("Entry updated.\n")
    else:
        print("No matching entry found.\n")

while True:
    print("PASSWORD MANAGER")
    print("1. Save new password")
    print("2. View all passwords")
    print("3. Search passwords")
    print("4. Delete an entry")
    print("5. Modify an entry")
    print("6. Exit")

    choice = input("Enter option: ")

    if choice == "1":
        platform = input("Enter site/app/platform name: ")
        username = input("Enter username/email: ")
        password = getpass.getpass("Enter password: ")
        save_password(platform, username, password)
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        search_password()
    elif choice == "4":
        delete_password()
    elif choice == "5":
        modify_password()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option.\n")
