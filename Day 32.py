'''
7) ?
------
---> This meta character will form a searching pattern as it will take any zero or one character for (?)
syntax ---> re.findall(".?, Variable_name)



import re
any = "This meta character"
an = re.findall("Th.?", any)
print(an)  

8) {}
------
---> This meta character will form a searching pattern as we mention the size in the {}
syntax ---> re.search("'.{size}, variable")  

import re
any = "This meta character will form a searching pattern as it will take any zero or one character"
an = re.findall(".{25}it", any)
print(an)   

9) |
-----
---> This meta character will form a searching pattern as it consider right or left any string is present or not for (|)


import re
any = "This meta character will form"
an = re.findall("that|will", any)
print(an)

10)\A
------

A special sequence is a \ followed by one of the characters in the list below, and has a

special meaning:
    
\A-
----
Returns a match if the specified characters are at the beginning of the string
Eg: "\AThe "

import re
txt = "The rain in spain"
# check if the string starts with "The":
x = re.findall(r"\AThe", txt)
if x:
    print("Yes, there is a match!")
else:
    print("No match")


11)\b(Word boundary)
-------------------
--->Returns a match where the specified character are at the beginning or at the end of a word
Eg: r"\bain" 

import re
txt = "The rain in spain"
x = re.findall("\d", txt)
if x:
    print("Yes, there is a match!")
else:
    print("No match")


12)\d
-------
--->\d → finds each digit separately
     If you want full numbers, use:  

import re
txt = "The rain in spain 123 is falling"
x = re.findall(r"\d", txt)

print(x)


13)\D-returns a match where the string does not contain digits (Non-digit)
--> "\D"  

import re
txt="The rain in 76 Spain"
#returns a match at every no-digit character
x=re.findall("\D",txt)
print(x)
if x:
    print("Yes,there is atleast one match!")
else:
    print("No match")

14)\s --> Returns a match where the string contains a white space character (Whitespace)
Eg: "\s" 

import re
txt = "The rain in spain"
x = re.findall("\s", txt)
print(x)
if x:
    print("Yes,there is atleast one match!")
else:
    print("No match")


Time and Date
--------------
%d ---> Day
%m ---> Month
%Y ---> Year
%H ---> Hour
%M ---> Min
%S ---> Sec
%P ---> AM/PM
%A ---> Day name(mon,tue,wed, thu, fri sat, sun)
%B ---> Month name

'''
import datetime
now = datetime.datetime.now()
print(now)

