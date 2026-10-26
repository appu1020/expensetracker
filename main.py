
#import json
from datetime import date
from storage import save_expenses, load_expenses
from expense_manager import add_expense, calculate_total, calculate_average, show_all_expenses, category_totals, delete_expense, search_expense


expenses = load_expenses()
today = date.today()


while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total spending")
    print("4. View average spending")
    print("5. View category-wise spending")
    print("6. Delete expense")
    print("7. Search expense")
    print("8. Exit")

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
        if not expenses:
            print("No expenses to show.")
        else:
            for category, total in category_totals().items():
                print(f"Category: {category}, Total: {total}")
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        name = input("Enter the name of the expense to search: ").strip()
        found_expenses = search_expense(name)
        if not found_expenses:
            print("No expenses found with that name.")
        else:
            for i, expense in enumerate(found_expenses, start=1):
                print(f"{i}. Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}") 

    elif choice == "8":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

    