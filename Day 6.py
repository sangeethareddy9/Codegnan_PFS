# Day 6 Practice

name = input("Enter name: ")
age = int(input("Enter age: "))

future_age = age + 5

count = 0

def visit():
    global count
    count = count + 1

visit()

print("Name:", name)
print("Age:", age)
print("Age after 5 years:", future_age)

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

print("Visited:", count)
