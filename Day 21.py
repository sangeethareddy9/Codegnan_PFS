'''
MODULES
------

---> A module in python is simple file that contain python code(variables, functions, classes)
---> To use module, we have to use a keyword called import before the module.
1). Built or inbuilt
2). User-defined modules




import import_module
print(import_module.div(6,9)) 

import Assignments
print(Assignments.count_vowels)


#USER-DEFINE MODULE
-------------------
--->This is developed by the user or programmer inside a file of file or python code and used by called import with filename...

#syntax---> import(keyword) file_name
            file_name.functionality 


import import_module
print(import_module.add(8,9))




#BUILT-IN OR INBUILT
--------------------

--->Already these are comes with installation and they ready to use in the program
---> This is developed by the developer 


import math
print(math.sqrt(25)) 



import random
print(random.randint(1, 100)) '''


import random

win = 0

while win < 3:
    num = random.randint(1,5)
    guess = int(input())

    if guess == num:
        print("correct")
        win += 1
    else:
        print("Not correct")

        
                


