'''#break

#When break is used, the loop ends immediately, when we found the required value.

for i in range(1, 6):
    print(i)
    if i == 3:
        break    

#inlists

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
    if num == 30:
        break        
    

#continue ----> continue is used to skip the current iteration and move to the next iteration of the loop.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)  

list = [10, 20, 30, 40, 50]

for i in list:
    if i == 20:
        continue
    print(i)  

#pass
#pass is a null statement (does nothing). this is called a space holder. incase any statement like (if, for , else, elif...)
#this should complete, if not we will get indentation error to avoid this we using pass 

for j in range(1,100):
    pass                   


#for loop --- else: it will fall block, when all loops are completed

for m in range(1,10):
    print(m)
else:
    print("else block")   

#whileloop ---> this is a combination for and if statements, if we did not,
#end the loop in proper way it will run upto the memory space until it becomes empty

num = 1
while num<5:
    print(num)   #it will give continuious output 1
    

num = 1
while num<5:
    print(num)
    num += 1  '''


user_in = int(input("Enter the limit : "))
num_1 = 0
num_2 = 1
print(num_1, num_2, end=" ")
for v in range(user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3, end=" ")





    


    
