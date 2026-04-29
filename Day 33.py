import re
def validate_name(name):
    pattern=r'^[A-Za-z]{3,}-$'
    return re.fullmatch(pattern,name)
def validate_email(email):
    pattern=r'^[\w\.-]+@[\w.-]+\.\w+$'
    return re.fullmatch(pattern,email)
def validate_phone(phone):
    pattern=r'^[0-9]{10}$'
    return re.fullmatch(pattern,phone)
def validate_password(password):
    pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=,*\d).{8,}$'
    return re.fullmatch(pattern,password)
def main():
    name=input("Enter Name: ")
    email=input("Enter Email: ")
    phone=input("Enter Phone Number: ")
    password=input("Enter password: ")
    if not validate_name(name):
        print("Invalid_Name")
    elif not validate_email(email):
        print("Inavlid email")
    elif not validate_phone(phone):
        print("Inavlid phone")
    elif not validate_password(password):
        print("Invalid password")
    else:
        print("All inputs are valid")

if __name__ == "__main__":
    main()


----------------------------------------------------------------------------------------------------------------------------------------------
Data analysis

#Useage
--------
this is critical because it converts raw data into actionable insights, enabling information to decision-making easy and improve
operational efficiency.

Impacts on:-
1.Decision-making
2.Improved Operational Efficiency
3.Customer Understanding
4.Market Insights
5.Risk Management
6.Data-Driven Strategies
