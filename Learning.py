# ------------------ TIME CONVERSION CHECK ------------------

time_a_day = input("Enter 24-hour time (HH:MM): ")

parts = time_a_day.split(":")
hours = int(parts[0])
minutes = int(parts[1])

if 13 <= hours <= 23 and 0 <= minutes < 60:
    print(time_a_day)   # corrected (removed quotes)
else:
    print("Invalid time or not in PM range")


# ------------------ LIST CONCEPT ------------------

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data.
# Other 3 are Tuple, Set, and Dictionary.

# Lists are created using square brackets []
# Example:
mylist = ["San", "Vis", "Ram"]

# Nested List Example
List = [1, 2, 3, "python", [1, 2, ["Python", "Java"], "Language"]]

# Accessing 'h' from "Python"
print(List[4][2][0][3])


# Another Nested Example
List_1 = [4, 5, 6, "Python", [4, 5, 6, "java", "c++", ["python", "java"], "language"]]

# Accessing 'v' from second "java"
print(List_1[4][5][1][2])


# ------------------ MUTABLE CONCEPT ------------------

# Mutable means "can be changed after creation"
# Immutable means "cannot be changed directly"
# List is mutable

# ------------------ LIST METHODS ------------------

# 1. append() --> This method is used to add a single item at the end of the list

nums = [9, 18, 27]
nums.append(4)
nums.append([36, 45])
nums.append("San")

# 2. extend() --> This method is used to add multiple items to the end of a list
# Each element (or character in a string) is added individually

nums.extend("San")
nums.extend("210")

print(nums)


# 3. remove() --> This method is used to remove a specific element from a list
# It removes only the first occurrence of the given value

a = [1, 2, 3, 2]

a.remove(2)
a.remove(2)

print(a)


# 4. pop() --> This method is used to remove an element using its index
# If no index is given, it removes the last element

a = [1, 2, 3, 9, 10]

a.pop(3)

print(a)
