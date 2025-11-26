# 🔐 Password Manager (Python)

A simple and beginner-friendly local password manager that stores passwords securely using SHA-256 hashing. This project demonstrates file handling, hashing, basic security concepts, and real-use case logic in Python.

---

## 🚀 Features
✔ Save a password for any site/app  
✔ SHA-256 hashing for security  
✔ View stored encrypted passwords  
✔ File auto-creation to prevent errors  
✔ Simple command-line interface

---

## 📂 Project Structure
password-manager/
│
├── main.py            # Main program logic
├── password.txt       # Storage file for hashed passwords
└── README.md          # Project description

---

## 🧠 How It Works
1. User runs the Python script  
2. Selects whether to save or view a password  
3. Passwords are hashed before storage  
4. File is automatically created if missing  
5. User can view stored encrypted entries anytime  

---

## ▶️ How to Run

### 1. Verify Python is installed  
python --version


### 2. Run the app
python main.py

PASSWORD MANAGER

1. Save new password
2. View saved passwords
Enter option number: 1
Enter site/app name: Instagram
Enter password: myPassword123
Password stored successfully!

Stored in file as:
Instagram : 2b7290c705f71f9d…

## 🛠️ Tech Used
- Python
- hashlib library
- os library
- text file storage

---

## 🌱 Future Improvements (coming soon)
✔ Master password  
✔ Input masking (hidden password typing)  
✔ Storing usernames  
✔ Search functionality  
✔ Delete/edit entries  
✔ GUI interface with Tkinter  
✔ Strong encryption using `cryptography` library  

---

## 👤 Author
Created by **Zainab Sultan Daniyal**  
GitHub: [ZainabSDaniyal](https://github.com/ZainabSDaniyal)