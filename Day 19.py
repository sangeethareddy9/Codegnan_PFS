'''#LAMBDA FUNCTIONS()
-------------------

---> This is also called anonymous function...
---> A lambda function can n number of arguments but have only one expression

SYNTAX
------
        lambda (keyword) arguments : expression

        

number = lambda S : S + 10
print(number(6))   

txt = lambda an, some, do : some - (some - an)* do
print(txt(9, 12, 21))

# Explanation:
# an = 9, some = 12, do = 21

# Step 1: (some - an) → 12 - 9 = 3
# Step 2: 3 * do → 3 * 21 = 63
# Step 3: some - result → 12 - 63 = -51

# Final Output: -51   


#SUBTRACTION

sub = lambda a, b: a - b
print(sub(10, 4))  


#MULTIPLICATION

mul = lambda S, V, R : S* R* V
print(mul(2, 30, 4)) 

#DIVISION

div = lambda V, S, R : V // R % S
print(div(2, 3, 14))  

#LIST COMPREHENSION:
--------------------
---> This is offers the shorter syntaxhen you want to create a new list from the existing list


SYNTAX:
------  

variable_name = [expression loop and condition ]
'''

list_old = [5, 6, 7, 8, 9]
list_new = [x for x in list_old if x%2 == 0]
print(list_new)














