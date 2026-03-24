# Strings in python are sequence of characters and can be written using single or double quotes

# -------------------------------
# INDEXING
# used to access characters using position (starts from 0)
# -------------------------------
text = "Hello World"
print("indexing:", text[6])

# -------------------------------
# SLICING
# used to get a part of string using start and end index
# -------------------------------
name = "Sangeetha Reddy"
print("slicing:", name[3:10])


# -------------------------------
# IMMUTABILITY & REPLACE
# strings cannot be changed directly, but we can create new string using replace()
# -------------------------------
lang = "Python Programming"
new_lang = lang.replace("Python", "Java")
print("after replace:", new_lang)
# print(lang)   # original stays same


# -------------------------------
# STRING SLICING PRACTICE
# -------------------------------
day = "Iam Sangeetha from Rajamundry, Iam a Masters of Computer Applications from Andhra University in 2025 with 8.53CGPA."

print("slice 1:", day[5:15])
print("slice 2:", day[20:31])
print("slice 3:", day[-40:-23])

# -------------------------------
# REVERSING A STRING
# using slicing with step -1
# -------------------------------
print("reverse:", day[::-1])
print("reverse step 2:", day[::-2])

# -------------------------------
# LENGTH OF STRING
# len() function gives total number of characters
# -------------------------------
print("length:", len(day))

# -------------------------------
# SPLIT METHOD
# used to convert string into list based on separator
# -------------------------------
print("words:", day.split(" "))


# -------------------------------
# SPLIT WITH SUBSTRING
# -------------------------------
some = "python is a programming language"
print("split word:", some.split("programming"))


# -------------------------------
# LOWER & REPLACE
# lower() converts to lowercase
# replace() replaces part of string
# -------------------------------
print("lower:", some.lower())
print("replace:", some.replace("programming", "normal"))


# -------------------------------
# MEMBERSHIP OPERATOR
# used to check if substring exists in string
# -------------------------------
if "python" in some:
    print("yes it is there")
else:
    print("no it is not there")


# -------------------------------
# VOWELS COUNT (WITHOUT LOOP)
# using count() method
# -------------------------------
text2 = "Sangeetha"

print("a:", text2.count("a"))
print("e:", text2.count("e"))
print("i:", text2.count("i"))
print("o:", text2.count("o"))
print("u:", text2.count("u"))

total = (text2.count("a") + text2.count("e") +
         text2.count("i") + text2.count("o") +
         text2.count("u"))

print("total vowels:", total)
