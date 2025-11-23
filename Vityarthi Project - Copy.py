import json

transactions = []
budgets = {}
DATA_FILE = "finance_data.json"

def save_data():
    """Saves the transactions and budgets to a JSON file."""
    data = {
        "transactions": transactions,
        "budgets": budgets
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully.")

def load_data():
    """Loads the transactions and budgets from a JSON file."""
    global transactions, budgets
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            transactions = data.get("transactions", [])
            budgets = data.get("budgets", {})
    except FileNotFoundError:
        print("No saved data found. Starting with empty records.")

def add_transaction():
    print("\n-- Add Transaction --")
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Travel, etc): ")
        txn = {"amount": amount, "category": category}
        transactions.append(txn)
        print("Transaction added.")
        save_data()
    except ValueError:
        print("Invalid amount. Please enter a number.")

def show_transactions():
    print("\n-- All Transactions --")
    if not transactions:
        print("No transactions yet.")
        return
    for i, t in enumerate(transactions, start=1):
        print(f"{i}. ₹{t['amount']} | {t['category']}")

def delete_transaction():
    print("\n-- Delete Transaction --")
    if not transactions:
        print("No transactions to delete.")
        return

    # show transactions with numbers
    show_transactions()

    try:
        idx = int(input("Enter the transaction number to delete (0 to cancel): "))
        if idx == 0:
            print("Delete cancelled.")
            return

        # convert 1-based index to 0-based
        if 1 <= idx <= len(transactions):
            removed = transactions.pop(idx - 1)
            print(f"Deleted transaction: ₹{removed['amount']} | {removed['category']}")
            save_data()
        else:
            print("Invalid transaction number.")
    except ValueError:
        print("Please enter a valid number.")

def set_budget():
    print("\n--- Set Budget ---")
    category = input("Enter category: ")
    try:
        amount = float(input("Enter budget amount: "))
        budgets[category] = amount
        print(f"Budget set for {category}: ₹{amount}")
        save_data()
    except ValueError:
        print("Invalid amount. Please enter a number.")

def check_budget():
    print("\n---Budget Status ---")
    if not budgets:
        print("No budgets set.")
        return

    spent = {}
    for t in transactions:
        cat = t["category"]
        spent[cat] = spent.get(cat, 0) + t["amount"]

    for cat, b_amt in budgets.items():
        used = spent.get(cat, 0)
        print(f"{cat}: Spent ₹{used} / Budget ₹{b_amt}")

        if used > b_amt:
            print("OVER BUDGET!")
        elif used >= 0.9 * b_amt:
            print("NEAR BUDGET LIMIT!")

def main():
    load_data()
    while True:
        print("\n==== SIMPLE FINANCE TRACKER =====")
        print("1. Add transaction")
        print("2. Show all transactions")
        print("3. Set budget")
        print("4. Check budget")
        print("5. Delete transaction")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_transactions()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            check_budget()
        elif choice == "5":
            delete_transaction()
        elif choice == "0":
            print("Goodbye")
            save_data()
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()