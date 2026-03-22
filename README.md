#  Bank Management System

A simple console-based Bank Management System built in Python using Object-Oriented Programming (OOP).

---

##  Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Menu Options](#menu-options)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)

---

## About

This project is a basic banking system that allows users to create savings or current accounts, deposit money, withdraw money, check balance, and view account details — all through a simple text-based menu in the terminal.

---

## Features

- ✅ Create Savings Account
- ✅ Create Current Account
- ✅ Deposit Money
- ✅ Withdrawal Money
- ✅ Balance Inquiry
- ✅ Account Details

---

## Requirements

- Python 3.x
- No external libraries needed
- Uses only built-in `random` module

---

## How to Run

1. Make sure Python 3 is installed on your system.
2. Save the file as `bank.py`.
3. Open terminal and run:

```bash
python bank.py
```

---

## Menu Options

When you run the program, you will see this menu:

```
----- Bank Management System -----
1. Create Account
2. Deposit Money
3. Withdrawal Money
4. Balance Inquiry
5. Account Details
6. Exit
```

| Option | Action |
|--------|--------|
| 1 | Create a new Savings or Current account |
| 2 | Deposit money into an existing account |
| 3 | Withdraw money from an existing account |
| 4 | Check account balance |
| 5 | View full account details |
| 6 | Exit the program |

---

## Project Structure

```
bank.py
│
└── class Bank
    ├── __init__()          → sets up empty account dictionary
    ├── main()              → shows menu, handles user input in a loop
    ├── saving_account()    → creates a savings account
    ├── current_account()   → creates a current account
    ├── deposit()           → deposits money into account
    ├── withdrawal()        → withdraws money from account
    ├── balance_inq()       → displays current balance
    └── account_display()   → displays full account details
```

---

## How It Works

### Account Storage

All accounts are stored in a dictionary inside the `Bank` object:

```
self.dic_id = {
    account_number : {
        "name"  : "Ram",
        "ph_no" : 9876543210,
        "bal"   : 500,
        "type"  : "Saving Account"
    }
}
```

- **Outer key** = unique account number
- **Inner value** = that user's details (name, phone, balance, type)
- Each new account is **added** to the dictionary without overwriting existing ones
- Supports **multiple users** simultaneously

### Account Number Generation

Each account gets a **random 10-digit account number** generated automatically:

```python
star = "".join([str(random.randint(0, 9)) for _ in range(10)])
acc_no = int(star)
```

### Minimum Balance Rule

- Both Savings and Current accounts require a **minimum opening balance of ₹100**
- If the amount entered is below 100, the account will not be created

### Deposit

- Asks for account number and deposit amount
- Adds amount directly to stored balance: `self.dic_id[no]["bal"] += ad`
- Shows updated balance after deposit

### Withdrawal

- Asks for account number and withdrawal amount
- Checks if **sufficient balance** exists before deducting
- If amount exceeds balance, shows `"Insufficient balance."` and cancels
- Deducts amount from stored balance: `self.dic_id[no]["bal"] -= ad`

### Error Handling

All user inputs are wrapped in `try/except` blocks:

| Input | Error Caught | Action |
|-------|-------------|--------|
| Menu option | `ValueError` | Prints message, restarts menu loop |
| Phone number | `ValueError` | Prints message, returns to menu |
| Opening balance | `ValueError` | Prints message, returns to menu |
| Account number | `ValueError` | Prints message, returns to menu |
| Deposit/Withdrawal amount | `ValueError` | Prints message, returns to menu |

---

## Known Limitations

- Data is stored **in memory only** — all accounts are lost when the program is closed
- No **PIN or password** protection for accounts
- No check for **duplicate account numbers** (extremely rare but possible with random generation)
- Phone number is stored as integer — leading zeros will be lost

---

## Future Improvements

- Save account data to a file (`.json` or `.csv`) so data is not lost on exit
- Add PIN/password for account security
- Add money transfer between accounts
- Add transaction history per account
- Add duplicate account number check
- Store phone number as string to preserve leading zeros