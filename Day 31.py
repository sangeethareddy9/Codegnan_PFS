'''
REGULAR EXPRESSION(Reg Ex)
--------------------------
---> This regular Expressions or RedEx is a sequence of characters that forms a searching pattern.
---> To use this we have to import re, which will unlock the package

Functions
-----------
1)Findall
----------
---> by using this function, it will find all sequence in the string
syntax --> re.findall(metachar, variable_name)

2)Search
---------
---> by using this function, it will only find first sequence in the string
syntax --> re.search("metachar", variable_name)

---> Metacharacters are special characters in RegEx that have a specific meaning (not treated as normal characters).
They help you define search patterns more powerfully.


import re

text = "apple bag dog egg fan hat"
result1 = re.findall(r'[a-g]', text)
result2 = re.findall(r'[aeh]', text)

print(result1)
print(result2)  


import re

text = "Apple BAG dog Egg FAN hat"
result = re.findall(r'[A-Z]', text)

print(result) 

import re

text = "My number is 9876543210"
result = re.search(r'\d+', text)

print(result.group())

2)DOT(.)
------
The dot (.) metacharacter in Regular Expressions is used to match any single character except a newline (\n).

import re
we = "hello"
the = re.findall(r'h.llo', we)
print(the)


import re
print(re.findall(r'.at', "cat bat rat"))


3)Caret(^)
-----------
This is used to find  the string is starting with the sequence or not
syntax --> re.findall("^This is", how )  

import re
how = "This is used to find the string is starting with the sequence
who = re.findall("^This is", how)
then = re.search
print(who)
print(then)


4)$
---
This is used to find the string is ending with the sequence or not
syntax --> re.findall("$", variable_name)  

import re
out = "This is used to find the string is ending with the sequence "
one = re.findall("sequence $", out)
two = r.search("This$", out)
print(one)
print(two)

5)*
----  
--->This meta character will form a searching pattern as it will take any zweo or more character for (*) 

import re
san = "This meta character will form a searching pattern as it will take any zweo or more character"
CH = re.findall("c. *ii", san)
NA = re.search("T. *", san)
print(CH)
print(NA)

6)+
---
---> The plus (+) metacharacter is used to match one or more occurrences of a character or pattern. '''

import re

text = "This meta character will form a seaching pattern as it will"
vk = re.findall("an.+y", text)
virat = re.search("T. ", text)
print(vk)
print(virat)



