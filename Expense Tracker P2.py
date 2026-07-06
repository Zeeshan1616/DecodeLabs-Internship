import sqlite3
from datetime import datetime
conn
DB_NAME = "expenses.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def get_expense():
    while True:
        amount = input("Enter expense amount: ")

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if amount < 0:
            print("Expense can't be negative.\n")
            continue

        return amount


def get_category():
    category = input("Category (food, transport, bills, other): ").strip().lower()
    if category not in ("food", "transport", "bills", "other"):
        category = "other"
    return category


def add_expense():
    amount = get_expense()
    category = get_category()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
        (amount, category, date)
    )
    conn.commit()
    conn.close()

    print(f"Added {amount:.2f} to '{category}'.\n")


def view_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, amount, category, date FROM expenses ORDER BY id")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n==================================================")
    print(f"{'ID':<4}{'Amount':<12}{'Category':<12}{'Date'}")
    print("==================================================")
    for row in rows:
        expense_id, amount, category, date = row
        print(f"{expense_id:<4}{amount:<12.2f}{category:<12}{date}")
    print("==================================================\n")


def print_summary():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT amount, category FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    print("\n==============================")
    print("        EXPENSE SUMMARY")
    print("==============================")

    if not rows:
        print("No expenses recorded.\n")
        return

    amounts = [r[0] for r in rows]
    total = sum(amounts)
    count = len(amounts)
    average = total / count
    highest = max(rows, key=lambda r: r[0])
    lowest = min(rows, key=lambda r: r[0])

    print(f"Total expenses entered : {count}")
    print(f"Total spent            : {total:.2f}")
    print(f"Average expense        : {average:.2f}")
    print(f"Highest expense        : {highest[0]:.2f} ({highest[1]})")
    print(f"Lowest expense         : {lowest[0]:.2f} ({lowest[1]})")

    print("\nBreakdown by category:")
    categories = {}
    for amount, category in rows:
        categories[category] = categories.get(category, 0) + amount

    for cat, amt in categories.items():
        print(f"  {cat:<10}: {amt:.2f}")

    print("==============================\n")


def main():
    init_db()
    print("Expense Tracker - DecodeLabs")
    print("Data is saved to expenses.db\n")

    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. View summary")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()