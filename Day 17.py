'''
#functions()
#A function is a block of code which only runs when it is called.
#A function can return data as a result.
#A function helps avoiding code repetition.
#Two types of functions 1. Built_in or in-build
#                        2. User_defined

1. built-in functions()
---> They comes with the program itself and those are already defines....
eg..
-----print(), sum(), map().....

2. User defined Functions()
---> Thos is created by person who is developing or using for development.

*NOTE -
---> In Python, a function is defined using the def keyword,
followed by a function name and parentheses:

EXAMPLE: 
def my_function():
  print("Hello from a function")

#CALLING A FUNCTION

def my_function(here what we write are called parameters):
  print("Hello from a function")

my_function(here what we write is Arguments) 

#even numbers code:

def check_even(num):
    if num % 2 == 0:
        print(f"{num} is an Even number")
    else:
        print(f"{num} is an Odd number")

# function call
num = int(input("Enter a number: "))
check_even(num = 2)



#prime number in a functions

prime_num = int(input("Enter a number: "))
count = 0
def prime_check(num, count):
    for x in range(1, num+1):
        if num % x == 0:
            count += 1
    if count == 0:
        print("Prime")
    else:
        print("Not prime")
            
prime_check(prime_num, count)



#palindrome
def check_palindrome(text):
    rev = ""

    for ch in text:
        rev = ch + rev  

    if text == rev:
        print("Palindrome")
    else:
        print("NOT a Palindrome")

# function call
word = input("Enter a word: ")
check_palindrome(word)


#REQUIRED ARGUMENTS ---> Required arguments are the parameters that must be given values when calling a function.

num = 9
num_2 = 10
def add(num, num_2):
    print(num)
add(num, num_2)  


#DEFAULT ARGUMENTS ---> Default arguments are parameters that have a predefined value in a function.

my_name = "Sangeetha"
def add(my_name):
    print(my_name)

add(my_name = "Reddy")
add(my_name = "Chirla")  

#PRIME NUMBER DEFAULT ARGUMENTS CHECK

def prime_check(num=7):   # default number is 7
    count = 0
    
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    
    if count == 2:
        print(f"{num} is Prime")
    else:
        print(f"{num} is Not Prime")

#Function calls
prime_check()       #uses default value
prime_check(10)     #user value


#
def prime_num(num, count):
    for j in range(1, num + 1):
        if num % j == 0:
            count += 1

    if count == 2:
        print(f"{num} is a prime")
    else:
        print(f"{num} is not a prime")
prime_num(num = 13, count = 0)
prime_num(num = 67, count = 0)   


#
def so(txt, txt_3, txt_2):
    print(f"txt = {txt}, txt_2 = {txt_2}, txt_3 = {txt_3}")

so(txt_2 = 6, txt = 0, txt_3 = 70)  '''


def so(*Candidate_):  #Adding a star(*) before the parameter name in the function , recieve a tuple of arguments and can access items with indexes
    print(Candidate_)
so("San", "Ram", "Vis")





  



