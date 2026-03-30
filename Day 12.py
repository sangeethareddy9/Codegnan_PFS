''' Write a Python program to read a paragraph and count the number of vowels, consonants,
    and spaces using for loops.
    Print the length of the paragraph and display the counts of vowels, consonants, and spaces separately. 


paragraph = """Education is the key to success in life.
It helps us gain knowledge and develop skills.
Hard work and dedication are important to achieve our goals.
We should always be curious and keep learning new things.
A positive attitude makes our journey easier and meaningful."""

count_spaces = 0
count_vowels = 0
count_consonants = 0

#spaces
for ch in paragraph:
    if ch == " ":
        count_spaces += 1

#vowels
for ch in paragraph:
    if ch in "aeiouAEIOU":
        count_vowels += 1

#consonants
for ch in paragraph:
    if ch.isalpha() and ch not in "aeiouAEIOU":
        count_consonants += 1

print("Length of paragraph is:", len(paragraph))
print("Number of spaces:", count_spaces)
print("Number of vowels:", count_vowels)
print("Number of consonants:", count_consonants)  


#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

a = 9
print(b)
for j in range(1,10):
    print(j)   #it will be error because there is a difference between initial variable and normal variable 

#now
a = 9
for j in range(1,100):
    print(j) 

#range() ---> this is used to generate number
#syntax ---> range(start, end, step)

for j in range (1,30,3):   #we have to give "3" to move two positions okay
    print(j)
 

any = "abc"
print(list(any))
print(tuple(any))

any = "123"
print(int(any))
print(list(any))
print(tuple(any))  

so = 123
print(str(so))
print(type(so))  


an = [a1,b : 2, c : 3]
vs = str(an)
print(type(vs))
print(vs)
#print(tuple(an))
print(dict(an)) 

# [::-1] reverse


name = "Sangeetha"
print(name[::-1]) 

name = "Sangeetha"
rev = ""

for j in name:
    rev = j + rev
    print(rev) '''

name = input("Enter a string: ")
rev = ""

for j in name:
    rev = j + rev

if name == rev:
    print("Palindrome")
else:
    print("Not Palindrome")




