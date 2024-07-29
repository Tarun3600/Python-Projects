from expenses import Expense
import calendar
import datetime

def main():
    print("🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input for expense
    expense = get_user_expense()

    # Write it to the file
    save_expense_to_file(expense, expense_file_path)

    # Read the file and print the expenses
    summarize_expenses(expense_file_path, budget)

def get_user_expense():
    print("💰 Enter the expense details:")
    expense_name = input("📋 Enter the expense name: ")
    expense_amount = float(input("💵 Enter the expense amount: "))    
    print(f"✅ You entered: {expense_name} and ${expense_amount:.2f}")

    expense_categories = [
        "🍔 Food", 
        "🏡 Home", 
        "💼 Work", 
        "🎉 Fun", 
        "🗂️ Misc"
    ]

    while True:
        print("🔍 Select the expense category:")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"Enter the category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("❌ Invalid category selected. Please try again.")

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"💾 Saving user expense: {expense} to file: {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path, budget):
    print("📊 Summarizing user expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")   
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("📈 Summary of expenses by category:")
    for key, amount in amount_by_category.items():
        print(f"  {key} : ${amount:.2f}")

    total_spent = sum(expense.amount for expense in expenses)
    print(f"💸 You've spent ${total_spent:.2f} so far!")

    remaining_budget = budget - total_spent
    print(f"💰 Remaining budget: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    print(f"📅 Remaining days in the month: {remaining_days}")
    daily_allowance = remaining_budget / remaining_days
    print(f"📊 Daily allowance: ${daily_allowance:.2f}")

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == '__main__':
    main()
