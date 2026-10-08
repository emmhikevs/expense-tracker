import calendar
import datetime

from typing import List
from expense import Expense

def main():
    print(f"🚀 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 100000.00  # Set a budget for the user

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses (Pass both arguments here)
    summarize_expenses(expense_file_path, budget) 
    

def get_user_expense():
    print(f"🚀 Getting user expenses")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "🍔 Food", 
        "🚗 Transportation", 
        "🎉 Entertainment", 
        "💡 Utilities", 
        "🧾 Other",
    ]

    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print(f"Invalid category. Please try again!")

def save_expense_to_file(expense, expense_file_path):
    print(f"🚀 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expenses(expense_file_path, budget):
    print(f"Summarizing User Expenses")
    expenses: List[Expense] = []
    
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, category=expense_category, amount=float(expense_amount)
            )
            expenses.append(line_expense)

    amounts_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amounts_by_category:
            amounts_by_category[key] += expense.amount
        else:
            amounts_by_category[key] = expense.amount

    print("Expenses By Category:")
    for key, amount in amounts_by_category.items():
        print(f"Category: {key}, Total Amount: ${amount:.2f}")       

    total_spent = sum(expense.amount for expense in expenses)
    print(f"Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"Remaining Budget: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0
    print(green(f"Daily Budget for the rest of the month: ${daily_budget:.2f}"))

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()