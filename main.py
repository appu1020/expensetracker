
import json

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)



def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

expenses = load_expenses()

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
                print("Amount cannot be negative. Please enter a valid amount.")
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
        "category": category
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

category_total = category_totals()
#for category, total in category_total.items():
    #print(f"Category: {category}, Total: {total}")





def show_all_expenses():
    for i, expense in enumerate(load_expenses(), start=1):
        print(f"{i}. Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}")
    return expenses 


def delete_expense():

    if not load_expenses():
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
    
    deleted_expense = expenses.pop(index)
    print(f"Deleted expense: {deleted_expense['name']}, Amount: {deleted_expense['amount']}, Category: {deleted_expense['category']}")
    save_expenses(expenses)
    return deleted_expense

#all_expense = show_all_expenses()


while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total spending")
    print("4. View average spending")
    print("5. View category-wise spending")
    print("6. Delete expense")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_all_expenses()
    elif choice == "3":
        total = calculate_total()
        print(f"Total expenses: {total}")

    elif choice == "4":
        #total = calculate_total()
        average = calculate_average(calculate_total())
        print(f"Average expense amount: {average}")
    elif choice == "5":
        for category, total in category_totals().items():
            print(f"Category: {category}, Total: {total}")
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")

    