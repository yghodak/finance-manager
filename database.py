import sqlite3

def create_connection():
    conn = sqlite3.connect('finance_manager.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Create a table for storing transactions (income and expenses)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL
    )''')
    
    # Create a table for savings goals
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS savings_goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        goal_name TEXT NOT NULL,
        target_amount REAL NOT NULL,
        current_amount REAL NOT NULL,
        due_date TEXT NOT NULL
    )''')

    conn.commit()
    conn.close()

# Call the function to create tables when running the script for the first time
if __name__ == "__main__":
    create_tables()
