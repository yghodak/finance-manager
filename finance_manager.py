import sqlite3
import datetime
import matplotlib.pyplot as plt

def visualize_transactions():
    transactions = get_transactions()
    
    categories = {}
    for transaction in transactions:
        category = transaction[3]  # Category is the 4th column
        amount = transaction[2]
        if category not in categories:
            categories[category] = 0
        categories[category] += amount
    
    categories_list = list(categories.keys())
    amounts_list = list(categories.values())
    
    plt.bar(categories_list, amounts_list)
    plt.xlabel("Categories")
    plt.ylabel("Amount")
    plt.title("Income and Expense by Category")
    plt.show()


# Function to add a transaction (income or expense)
def add_transaction(description, amount, category):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()

    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
    INSERT INTO transactions (description, amount, category, date)
    VALUES (?, ?, ?, ?)
    ''', (description, amount, category, date))
    
    conn.commit()
    conn.close()

# Function to get the balance (total income - total expenses)
def get_balance():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT SUM(amount) FROM transactions WHERE amount > 0')
    income = cursor.fetchone()[0] or 0  # If no income, return 0
    
    cursor.execute('SELECT SUM(amount) FROM transactions WHERE amount < 0')
    expenses = cursor.fetchone()[0] or 0  # If no expenses, return 0
    
    conn.close()
    
    return income + expenses

# Function to get all transactions
def get_transactions():
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    
    conn.close()
    
    return transactions

# Example usage:
if __name__ == "__main__":
    # Add some sample transactions
    add_transaction("Salary", 5000, "Income")
    add_transaction("Grocery", -150, "Expense")
    
    # Get balance and print transactions
    print(f"Current Balance: {get_balance()}")
    print("All Transactions:")
    for transaction in get_transactions():
        print(transaction)
