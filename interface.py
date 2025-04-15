import finance_manager

def display_menu():
    print("\n--- Personal Finance Management ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View All Transactions")
    print("5. Exit")

def main():
    while True:
        display_menu()
        
        choice = input("Select an option: ")
        
        if choice == '1':
            description = input("Enter income description: ")
            amount = float(input("Enter income amount: "))
            finance_manager.add_transaction(description, amount, "Income")
        
        elif choice == '2':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            finance_manager.add_transaction(description, -amount, "Expense")
        
        elif choice == '3':
            balance = finance_manager.get_balance()
            print(f"Current Balance: {balance}")
        
        elif choice == '4':
            transactions = finance_manager.get_transactions()
            print("\n--- Transactions ---")
            for transaction in transactions:
                print(transaction)
        
        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
