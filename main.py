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

expenses.append(expense)
expenses.append(expense2)

for expense in expenses:
    print(f"Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}")

total = 0
for expense in expenses:
    total += expense['amount']
print(f"Total expenses: {total}")

average = total/len(expenses)
print(f"Average expense: {average}")