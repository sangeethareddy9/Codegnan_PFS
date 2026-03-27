'''
a = [10, "hello", [1, 2, 3], 25, "python", [4, 5], 100, "world", [6, 7, 8]]

print(type(a[0]))   # int
print(type(a[1]))   # str
print(type(a[2]))   # list
print(type(a[3]))   # int
print(type(a[4]))   # str
print(type(a[5]))   # list
print(type(a[6]))   # int
print(type(a[7]))   # str
print(type(a[8]))   # list  



print(9+8)
print("Python" + "Programming")
print([1,2]+[3,4])


#Concatenation
#Joining two or more values with '+' value.

case -1

#You can concatenate only same data types

print("Hello" + "World")   # string + string
print([1,2] + [3,4])       # list + list
print(10 + 20)             # int + int

#Strings Join Without Space Automatically

#Space must be added manuallyStrings Join Without Space Automatically

#Space must be added manually

print("Hello" + "World")      # HelloWorld
print("Hello" + " " + "World")  # Hello World


Case - 2

#** if we try to concatenate two different data type it will give type error

# print("Hello" + 10)   #Error(because str and int) 


tuple() --->

#A tuple is a collection which is ordered and unchangeable.

#Tuples are written with round brackets.

Thing = (1, "San", [3,4], (6,7)) 

Thing = (12, 89, "Python", (23, "Teja", [67, "Python is a language", (7, 8), (8, ("Python", [34, 9]))]))
print(Thing[3][2][1][9])


Num = 9
Num_2 = 90
print(f"before swapping Num ={Num} and Num_2 = {Num_2}")
Num, Num_2 = Num_2, Num
print(f"After swapping Num = {Num} and Num_2 = {Num_2}") '''



leap_year = int(input("Enter Year: "))

if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
    print(f"Yes, {leap_year} is a leap year")
else:
    print(f"No, {leap_year} is not a leap year")

