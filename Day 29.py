#Handling Errors

#1.Try Block--->The try block will test a block of code for errors
'''
try:
    print(b)
'''
#2.Except Block--->This block will take care of any errors
'''
try:
    print(b)
except:
    print("This block can handle error")
'''
#3.Else Block--->to define a block of code to be executed if no error were raised
'''
try:
    a=5
    b=9
    print(a+c)
except:
    print("Error here")
else:
    print("No error in the code")

try:
    a=5
    b=9
    c=13
    print(b+c)
except:
    print("Error here")
else:
    print("No error in the code")
'''
#4.Finally Block---->This block wil execute either try block have any errors or no error
'''
try:
    a=5
    b=9
    print(a+c)
except:
    print("Error here")
else:
    print("No error in the code")

try:
    a=5
    b=9
    print(a+b)
except:
    print("Error here")
else:
    print("No error in the code")
finally:
    print("The try-except block is finished")

try:
    num_1= int(input("Enter a number: "))
    num_2 = int(input("Enter a number: "))
    result = num_1/num_2
except ValueError:
    print("Pls enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Name error is identified")
else:
    print(f"Result = (result)")
finally:
    print("Program is completed")
'''
