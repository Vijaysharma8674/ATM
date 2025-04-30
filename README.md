ATM Project (Python, OOP, SQLite, Logging)

Overview

This project simulates a simple ATM system using Python, applying principles of Object-Oriented Programming (OOP), SQLite3 for database management, and logging for tracking transactions.

The ATM system allows users to:
	•	Create an account manually by setting their account number and PIN.
	•	Log in using existing account credentials.
  . Deposit money.
	•	Withdraw money.
	•	Check account balance.
	•	Secure all transactions into a local SQLite database.
	•	Track all operations with timestamped logs without cluttering the console.

  Features
	•	Account Creation: User defines their own Account Number and 4-digit PIN.
	•	Login System: Validate user credentials before accessing the account.
	•	Balance Checking: View current account balance.
	•	Deposit/Withdraw Money: Safe transaction handling.
	•	Persistent Storage: Account details saved into a SQLite3 database.
	•	Transaction Logging: Every action is logged to atm_transactions.log with timestamps.
	•	Clean OOP Design: Separated logic into classes and modules.
  . Store the PIN securely.Use bycrypt to encrypt the password and bcrypt.checkpw to verify..
  Technologies Used
	•	Python 3
	•	SQLite3 (no external installation required)
	•	Python logging module
	•	Object-Oriented Programming (OOP)
	•	CLI (Command-Line Interface)
  . bcrypt (bcrypt.checkpw)
