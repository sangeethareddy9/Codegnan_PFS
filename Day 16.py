# 1. Right Triangle Pattern
def right_triangle():
    num = int(input("Enter the number: "))
    for i in range(num + 1):
        for j in range(i):
            print("*", end="")
        print()

# 2. Number Triangle-1
def number_triangle_1():
    num = int(input("Enter the number: "))
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

# 3. Pyramid Stars
def pyramid_stars():
    num = int(input("Enter a number: "))
    for i in range(num):
        print(" " * (num - i - 1), end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

# 4. Squares
def squares():
    num = int(input("Enter the number: "))
    for i in range(num):
        for j in range(num):
            print("*", end="")
        print()

# 5. Reverse Triangle
def reverse_triangle():
    num = int(input("Enter the number: "))
    for i in range(num):
        for j in range(num - i):
            print("*", end="")
        print()

# 6. Number Triangle-2
def number_triangle_2():
    num = int(input("Enter the number: "))
    for i in range(num + 1):
        for j in range(i):
            print(i, end="")
        print()

# 7. ATM Simulation
def atm_simulation():
    icic_roy_ac_details = {"Name": "Roy", "ATM PIN": "0007", "Balance": 5000}
    
    print("Welcome to ICIC bank")
    print("Please insert your card")
    
    atm_pin = input("Please enter your pin: ")
    
    if len(atm_pin) == 4:
        if atm_pin == icic_roy_ac_details["ATM PIN"]:
            print("The pin is correct")
            
            user_choice = int(input("Enter \n1. Withdraw: "))
            
            if user_choice == 1:
                money_w = int(input("Enter money you want to withdraw: "))
                
                if money_w <= icic_roy_ac_details["Balance"]:
                    icic_roy_ac_details["Balance"] -= money_w
                    print(f"Remaining balance is {icic_roy_ac_details['Balance']}")
                else:
                    print("Insufficient balance")
        else:
            print("You have entered an incorrect pin.")
    else:
        print("Please enter a 4 digit pin")


# Main Program
if __name__ == "__main__":
    print("Choose an option:")
    print("1. Right Triangle Pattern")
    print("2. Number Triangle-1")
    print("3. Pyramid Stars")
    print("4. Squares")
    print("5. Reverse Triangle")
    print("6. Number Triangle-2")
    print("7. ATM Simulation")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        right_triangle()
    elif choice == 2:
        number_triangle_1()
    elif choice == 3:
        pyramid_stars()
    elif choice == 4:
        squares()
    elif choice == 5:
        reverse_triangle()
    elif choice == 6:
        number_triangle_2()
    elif choice == 7:
        atm_simulation()
    else:
        print("Invalid choice")
