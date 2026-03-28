# -------------------------------
# Day 11: Dictionaries & Sets
# -------------------------------


# 🔹 Dictionary
# Definition: A dictionary is a collection of key:value pairs.

# Example
student = {"name": "Ram", "age": 20}
print("Dictionary:", student)

# Access value
print("Name:", student["name"])


# 🔹 Dictionary Methods

# keys() → returns all keys
print("Keys:", student.keys())

# values() → returns all values
print("Values:", student.values())

# get() → safe access
print("Get name:", student.get("name"))
print("Get marks:", student.get("marks", 0))   # default value


# -------------------------------

# 🔹 Set
# Definition: A set is a collection of unique elements.

# Example
s = {1, 2, 2, 3}
print("\nSet:", s)   # duplicates removed


# 🔹 Set Operations

a = {1, 2}
b = {2, 3}

# Union → combine both sets
print("Union:", a | b)

# Intersection → common elements
print("Intersection:", a & b)

# Difference → elements in a but not in b
print("Difference:", a - b)


# -------------------------------

# 🔹 Simple PIN Program

# Definition: Checks whether entered PIN is correct or not

pin = "1234"
user = input("\nEnter PIN: ")

if user == pin:
    print("Correct PIN")
else:
    print("Wrong PIN")
