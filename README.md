Password Protector
Description

This repository contains a simple password manager implemented in Python. It securely stores and retrieves account passwords using encryption. The master password and a generated key are used for encryption and decryption.
Features

    Secure Storage: Passwords are encrypted with the Fernet encryption.
    Easy to Use: Simple interface for adding and viewing passwords.
    File Handling: Uses password.txt for storing passwords and key.key for the encryption key.

    Running the Application

    Run the script.
    Enter the master password when prompted.
    Choose to add a new password or view existing ones:
        Add a password: Enter the account name and password.
        View passwords: Stored passwords will be displayed in decrypted form.
    Press 'q' to quit.
