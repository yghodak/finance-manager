# Personal Finance Manager

A simple Python application for managing personal finances, tracking income and expenses, and setting savings goals.

## Features

- 📊 Add and view income & expense entries
- 🧾 Categorize transactions
- 🗂 SQLite-based persistent storage
- 🧠 Easy-to-use graphical interface (via Tkinter)
- 💾 Backup and restore support with SQL dump
## Getting Started

Follow these steps to get your local environment set up for development and testing.

### Prerequisites

- Python 3.x
- SQLite (for database storage)

### Installing

1. Clone this repository to your local machine:
```bash
git clone https://github.com/yghodak/finance-manager.git
cd finance-manager
```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
---
## ▶️ Usage
Run the application with:
```bash
python finance_manager.py
```
You’ll be able to:

-Add income/expense records

-View transaction history

-Backup or restore the database

---
## 🗃️ Project Structure
```csharp
finance-manager/
├── finance_manager.py        # Main application script
├── interface.py              # GUI interface (Tkinter)
├── database.py               # Handles SQLite database
├── finance_manager.db        # SQLite database file
├── backup.sql                # SQL backup of the DB
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```
---
## 📦 Dependencies

-Python 3.x

-Tkinter (comes preinstalled with most Python distributions)

-SQLite3 (standard library)

Install all required packages using:
```bash
pip install -r requirements.txt
```
---

## 🧑‍💻 Author

  ### Made by Yash Ghodake✨
