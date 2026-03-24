''' Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello". 

Strings is a sequence of characters '''

'''
any = "Hello World"
print(any[6])   #index it starts with 0,1,2,3,4,5 , and also negative from back side like -1,-2,-3,-4,-5,-6 


any = 'Sangeetha Reddy'
print(any[3:10])

'''
#Slicing this also immutable , where i couldn't able to modify on that particular variable.

'''
any = "Python Programming"
so = any.replace("Python","Java")
print(so)
#print(any)
'''

'''
day = " Iam Sangeetha from Rajamundry, Iam a Masters of Computer Applications from Andhra University in 2025 with 8.53CGPA."
#print(f"My name is {day[5:15]}")
#print(f"My location is {day[20:31]}")
#print(f"My college name is {day[-40:-23]}")
#print ({day[ ::-1]})
#print ({day[ ::-2]})
#print ({day[ ::-3]})
#print ({day[ 1::]})
#print ({day[ 2::]})
#print(len(day))
print(day.split(" "))
'''





#syntax variables_name.split("substring")
some = ("python is a programming language")
print (some.split("programming"))

#lower() --->this is used to convert all letters into lowercase



