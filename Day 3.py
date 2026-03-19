# expense_calculator.py

print("=" * 50)
print("💰 Expense Calculator".center(50))
print("=" * 50)

name = input("Enter your name: ")
income = float(input("Enter your monthly income: "))

print("\nEnter your expenses 👇")
food = float(input("Food: "))
travel = float(input("Travel: "))
entertainment = float(input("Entertainment: "))
others = float(input("Others: "))

total_expense = food + travel + entertainment + others
balance = income - total_expense
savings = (balance / income) * 100

print("\n" + "=" * 50)
print("Name:", name)
print("Income:", income)
print("Total Expenses:", total_expense)
print("Balance:", balance)
print("Savings %:", round(savings, 2))
print("=" * 50)

if balance > 0:
    print("😊 You are saving money!")
elif balance == 0:
    print("😐 You spent exactly your income.")
else:
    print("⚠️ You are overspending!")


    #NEW ONE


# rectangle.py

print("📐 Rectangle Calculator")

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("\n--- Result ---")
print("Area:", area)
print("Perimeter:", perimeter)
