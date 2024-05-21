# Bank Application

This is a simple console-based bank application implemented in Python. It allows users to log in, deposit money, and transfer funds. The application uses basic file handling for recording transactions.

Code Overview

`Bank` Class

The `Bank` class encapsulates the functionality of the bank application. It has methods for logging in, depositing money, transferring money, and starting the application.

 Methods

- `__init__(self)`: Initializes the `account_details` dictionary to store account balances.

- `log_in(self)`: 
  - Prompts the user for a username and password.
  - Writes hardcoded account details to `account_details.txt`.
  - Checks if a specified directory exists.
  - Validates the password against a hardcoded value (`12345`) and prints a welcome message if successful or an error message otherwise.

- `deposit(self)`:
  - Prompts the user for an account name and an amount to deposit.
  - Updates the account balance in the `account_details` dictionary.
  - Writes a deposit receipt to `deposit_reciept.txt`.

- `transfer(self)`:
  - Prompts the user for an amount to transfer.
  - Prints a message indicating the transfer amount.
  - Writes a transfer receipt to `Transfer_reciept.txt`.

- `start(self)`:
  - Displays a menu with options to log in, deposit money, transfer money, or exit the program.
  - Handles user input to call the appropriate method based on the selected option.

Usage

1. **Running the Application**:
    - Run the script using Python: `python bank.py`
    - Follow the on-screen prompts to log in, deposit money, or transfer funds.

Example

Here is a step-by-step example of how the application can be used:

1. **Log In**:
    - Enter a username.
    - Enter the password (`12345`).

2. **Deposit Money**:
    - Select the deposit option.
    - Enter the account name.
    - Enter the amount to deposit.

3. **Transfer Money**:
    - Select the transfer option.
    - Enter the amount to transfer.

4. **Exit**:
    - Select the exit option to close the application.

 Notes

- The password for logging in is currently hardcoded as `12345`.
- The directory path in the `log_in` method is set to `r"C:\Users\User\OneDrive\Desktop\New folder (2)"`. You may need to update this path to a valid directory on your system.
- The application writes receipts for deposits and transfers to text files in the same directory as the script.


