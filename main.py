


expenses = []

expense = {
    "name": "lunch",
    "amount": 500,
    "category": "food"


}
expense2 = {
    "name": "bus",
    "amount": 200,
    "category": "transport"
}

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    expense3 = {
        "name": name,
        "amount": amount,
        "category": category
    }
    expenses.append(expense3)

expenses.append(expense)
expenses.append(expense2)

for expense in expenses:
    print(f"Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}")

def calculate_total():
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total expenses: {total}")
    return total


total = calculate_total()

def calculate_average(total):
    if len(expenses) == 0:
        return 0
    else:
        average = total / len(expenses)
        return average

average = calculate_average(total)
print(f"Average expense amount: {average}")

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
for category, total in category_total.items():
    print(f"Category: {category}, Total: {total}")





def show_all_expenses():
    for expense in expenses:
        print(f"Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}")
    return expenses
all_expense = show_all_expenses()

while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total spending")
    print("4. View average spending")
    print("5. View category-wise spending")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_all_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        total = sum(expense["amount"] for expense in expenses)
        average = total / len(expenses)
        print(f"Average expense amount: {average}")
    elif choice == "5":
        for category, total in category_totals().items():
            print(f"Category: {category}, Total: {total}")
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

    