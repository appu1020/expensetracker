
from storage import load_expenses,save_expenses
from datetime import date


expenses = load_expenses()
today = date.today()

def add_expense():
    while True:
        name = input("Enter expense name: ").strip()
        if not name:
            print("Expense name cannot be empty. Please enter a valid name.")
            continue
        break

    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount cannot be negative or zero. Please enter a valid amount.")
                continue
            
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")


    while True:
        category = input("Enter expense category: ").strip()
        if not category:
            print("Expense category cannot be empty. Please enter a valid category.")
            continue
        break

    expense3 = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": str(today)
    }
    expenses.append(expense3)
    save_expenses(expenses)



#for expense in expenses:
   # print(f"Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}")

def calculate_total():
    total = 0
    for expense in expenses:
        total += expense['amount']
    #print(f"Total expenses: {total}")
    return total


#total = calculate_total()

def calculate_average(total):
    if len(expenses) == 0:
        return 0
    else:
        average = total / len(expenses)
        return average


def category_totals():
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return category_totals

#category_total = category_totals()
#for category, total in category_total.items():
    #print(f"Category: {category}, Total: {total}")





def show_all_expenses():

    if not expenses:
        print("No expenses to show.")
        return None
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense.get('date', 'N/A')}")


def delete_expense():

    if not expenses:
            print("No expenses to delete.")
            return None
    show_all_expenses()
    while True:
        try:
            index = int(input("Enter the index of the expense to delete: ")) - 1
            if index < 0 or index >= len(expenses):
                print("Invalid index. Please enter a valid index.")
                continue
            
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    while True:
        ans = input(f"Are you sure you want to delete the expense '{expenses[index]['name']}'? (y/n): ").strip().lower()
        if ans == 'n':
            print("Deletion cancelled.")
            return None
        elif ans != 'n' and ans != 'y':
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        else:
            deleted_expense = expenses.pop(index)
            print(f"Deleted expense: {deleted_expense['name']}, Amount: {deleted_expense['amount']}, Category: {deleted_expense['category']}")
            save_expenses(expenses)
            return deleted_expense
            

#all_expense = show_all_expenses()

def search_expense(name):
    while True:
        if not name:
            print("Expense name cannot be empty. Please enter a valid name.")
            name = input("Enter the name of the expense to search: ").strip()
            continue

        else:       
            found_expenses = [expense for expense in expenses if  name.lower() in expense['name'].lower()]
            return found_expenses