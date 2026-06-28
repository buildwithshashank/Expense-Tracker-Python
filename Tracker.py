import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self,amount,description):
        expense = {
            "amount": amount,
            "description": description,
        }
        self.expenses.append(expense)
    
    def view_expenses(self):
        for expense in self.expenses:
            print(expense["description"], "- Rs.", expense["amount"])
    
    def get_total(self):
        total = 0
        for expense in self.expenses:
            total = total + expense["amount"]
        return total

    def delete_expense(self, index):
        self.expenses.pop(index)

    def save_to_file(self):
        file = open("expenses.txt", "w")
        file.write(json.dumps(self.expenses))
        file.close()

    def load_from_file(self):
        try:
            file = open("expenses.txt", "r")
            data = file.read()
            self.expenses = json.loads(data)
            file.close()
        except:
            self.expenses = [0]
        



tracker = ExpenseTracker()
tracker.load_from_file()

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Get Total")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Choose number of your choice: ")
    if choice == "1":
        amount = int(input("Toal amount spent: "))
        description = input("The Purpose of expenditure: ")
        tracker.add_expense(amount, description)
        print("Expense added!")
        tracker.save_to_file()

    elif choice == "2":
        tracker.view_expenses()

    elif choice =="3":
        print("Total expense: ",tracker.get_total())

    elif choice =="4":
        tracker.view_expenses()
        index = int(input("Enter Index of the Expense(): "))
        tracker.delete_expense(index)
        print("Expense deleted!")
        tracker.save_to_file()

    elif choice == "5":
        print("Goodbye!")
        break

    
    

        

        

    
 