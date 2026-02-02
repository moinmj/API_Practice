# import csv
# def write_expense():
#     Date=input("Enter the date")
#     Amount=input("Enter the amount")
#     Category=input("Enter the category")
# # my data rows as dictionary objects
#     mydict = [{"Date":Date , 
#            "Amount":Amount ,
#            "Category":Category }]

# # field names
# fields = ['date', 'amount', 'category']

# # name of csv file
# filename = "expense.csv"

# # writing to csv file
# with open(filename, 'w',newline='') as csvfile:
#     # creating a csv dict writer object
#     writer = csv.DictWriter(csvfile, fieldnames=fields)

#     # writing headers (field names)
#     writer.writeheader()

#     # writing data rows
#     writer.writerows(write_expense)
# # Open the CSV file for reading
# with open('expense.csv', mode='r') as file:
#     # Create a CSV reader with DictReader
#     csv_reader = csv.DictReader(file)

#     # Initialize an empty list to store the dictionaries
#     data_list = []

#     # Iterate through each row in the CSV file
#     for row in csv_reader:
#         # Append each row (as a dictionary) to the list
#         data_list.append(row)

# # Print the list of dictionaries
# for data in data_list:
#     print(data)
# write_expense()
# import csv

# # File to store expenses
# filename = "expenses.csv"

# # Function to add expense
# def add_expense(date, amount, category):
#     expense = {"date": date, "amount": amount, "category": category}
    
#     with open(filename, mode='a', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=["date", "amount", "category"])
        
#         # Write header if file is empty
#         file.seek(0)
#         if file.tell() == 0:
#             writer.writeheader()
        
#         writer.writerow(expense)
#     print("✅ Expense added successfully.")

# # Function to view all expenses
# def view_expenses():
#     try:
#         with open(filename, mode='r') as file:
#             reader = csv.DictReader(file)
#             print("\n📋 All Expenses:")
#             for row in reader:
#                 print(f"📅 {row['date']} | 💰 Rs.{row['amount']} | 🏷️ {row['category']}")
#     except FileNotFoundError:
#         print("⚠️ No expenses recorded yet.")

# # Main Menu
# def main():
#     while True:
#         print("\n🔹 Expense Tracker Menu:")
#         print("1. Add Expense")
#         print("2. View Expenses")
#         print("3. Exit")
        
#         choice = input("Enter your choice (1/2/3): ")

#         if choice == '1':
#             date = input("Enter date (YYYY-MM-DD): ")
#             amount = input("Enter amount: ")
#             category = input("Enter category (e.g., Food, Travel, Bills): ")
#             add_expense(date, amount, category)
        
#         elif choice == '2':
#             view_expenses()
        
#         elif choice == '3':
#             print("👋 Exiting. Thank you!")
#             break
#         else:
#             print("❌ Invalid choice. Try again.")

# # Run the program
# main()
# import csv
# from collections import defaultdict

# filename = "expenses.csv"

# # Add an expense
# def add_expense(date, amount, category):
#     expense = {"date": date, "amount": amount, "category": category}
    
#     with open(filename, mode='a', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=["date", "amount", "category"])
#         file.seek(0)
#         if file.tell() == 0:
#             writer.writeheader()
#         writer.writerow(expense)
#     print("✅ Expense added successfully.")

# # View all expenses
# def view_expenses():
#     try:
#         with open(filename, mode='r') as file:
#             reader = csv.DictReader(file)
#             print("\n📋 All Expenses:")
#             for row in reader:
#                 print(f"📅 {row['date']} | 💰 Rs.{row['amount']} | 🏷️ {row['category']}")
#     except FileNotFoundError:
#         print("⚠️ No expenses recorded yet.")

# # Summary by Date
# def summary_by_date():
#     totals = defaultdict(float)
#     try:
#         with open(filename, mode='r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 totals[row['date']] += float(row['amount'])
#         print("\n📊 Summary by Date:")
#         for date, total in totals.items():
#             print(f"📅 {date} -> Rs.{total:.2f}")
#     except FileNotFoundError:
#         print("⚠️ No expenses to summarize.")

# # Summary by Category
# def summary_by_category():
#     totals = defaultdict(float)
#     try:
#         with open(filename, mode='r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 totals[row['category']] += float(row['amount'])
#         print("\n📊 Summary by Category:")
#         for cat, total in totals.items():
#             print(f"🏷️ {cat} -> Rs.{total:.2f}")
#     except FileNotFoundError:
#         print("⚠️ No expenses to summarize.")

# # Main Menu
# def main():
#     while True:
#         print("\n🔹 Expense Tracker Menu:")
#         print("1. Add Expense")
#         print("2. View Expenses")
#         print("3. Summary by Date")
#         print("4. Summary by Category")
#         print("5. Exit")
        
#         choice = input("Enter your choice (1-5): ")

#         if choice == '1':
#             date = input("Enter date (YYYY-MM-DD): ")
#             amount = input("Enter amount: ")
#             category = input("Enter category (e.g., Food, Travel, Bills): ")
#             add_expense(date, amount, category)

#         elif choice == '2':
#             view_expenses()

#         elif choice == '3':
#             summary_by_date()

#         elif choice == '4':
#             summary_by_category()

#         elif choice == '5':
#             print("👋 Exiting. Thank you!")
#             break
#         else:
#             print("❌ Invalid choice. Try again.")

# # Run the app
# main()
import csv
from collections import defaultdict

filename = "expenses.csv"

# Add an expense
def add_expense(date, amount, category):
    try:
        amount = float(amount) #declare
        #Formation of dict
        expense = {"date": date, "amount": f"{amount:.2f}", "category": category}
        #method in csv to write in file csv.DictWriter(file,fieldnames/headers=[])
        with open(filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["date", "amount", "category"])
            # file.seek(0)
            # if file.tell() == 0:
            #method in csv to write header and here header are date,amount,category
            writer.writeheader()
            #method to recieve/write row data
            writer.writerow(expense)
        print("✅ Expense added successfully.")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

# View all expenses
def view_expenses():
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            print("\n📋 All Expenses:")
            for row in reader:
                print(f"📅 {row['date']} | 💰 Rs.{row['amount']} | 🏷️ {row['category']}")
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.")

# Summary by Date
def summary_by_date():
    totals = defaultdict(float)
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    totals[row['date']] += float(row['amount'])
                except (ValueError, KeyError):
                    continue
        print("\n📊 Summary by Date:")
        for date, total in totals.items():
            print(f"📅 {date} -> Rs.{total:.2f}")
    except FileNotFoundError:
        print("⚠️ No expenses to summarize.")

# Summary by Category
def summary_by_category():
    totals = defaultdict(float)
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    totals[row['category']] += float(row['amount'])
                except (ValueError, KeyError):
                    continue
        print("\n📊 Summary by Category:")
        for cat, total in totals.items():
            print(f"🏷️ {cat} -> Rs.{total:.2f}")
    except FileNotFoundError:
        print("⚠️ No expenses to summarize.")

# Main Menu
def main():
    while True:
        print("\n🔹 Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary by Date")
        print("4. Summary by Category")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = input("Enter amount: ")
            category = input("Enter category (e.g., Food, Travel, Bills): ")
            add_expense(date, amount, category)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            summary_by_date()

        elif choice == '4':
            summary_by_category()

        elif choice == '5':
            print("👋 Exiting. Thank you!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    main()
