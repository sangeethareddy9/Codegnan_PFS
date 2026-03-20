# day4

print("🔁 Expense Calculator with Loop")

while True:
    name = input("\nEnter your name: ")
    income = float(input("Enter your monthly income: "))

    food = float(input("Food expense: "))
    travel = float(input("Travel expense: "))
    entertainment = float(input("Entertainment expense: "))
    others = float(input("Other expenses: "))

    total = food + travel + entertainment + others
    balance = income - total

    print("\n--- Result ---")
    print("Name:", name)
    print("Total Expense:", total)
    print("Balance:", balance)

    if balance > 0:
        print("😊 You are saving money!")
    elif balance == 0:
        print("😐 Balanced spending.")
    else:
        print("⚠️ Overspending!")

    choice = input("\nDo you want to calculate again? (yes/no): ")
    if choice.lower() != "yes":
        print("Thank you! 👋")
        break
