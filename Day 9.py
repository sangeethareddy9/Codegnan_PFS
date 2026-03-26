''' time_a_day = input("Enter 24-hour time (HH:MM): ")

parts = time_a_day.split(":")
hours = int(parts[0])
minutes = int(parts[1])

if 13 <= hours <= 23 and 0 <= minutes < 60:
    print("Time_a_day")
else:
    print("Invalid time or not in PM range")


List --->Lists are used to store multiple items in a single variable

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
example : mylist = ["San", "vis", "Ram"] 

List = [1,2,3,"python", [1,2,["Python", "Java"], "Language"]]
print(List[4][2][0][3])



List_1 = [4, 5, 6, "Python", [4, 5, 6, "java", "c++", ["python", "java"], "language"]]
print(List_1[4][5][1][2])
               
append() --- this method is used to add new items

1. append() → Add element at end ..Mutable means "can be changed after creation", Immutable means "cannot modify directly on the variable " list is mutable. 

nums = [9, 18, 27]
nums.append(4)
nums.append([36,45])
nums.append("San")
nums.extend("San")
nums.extend("210")
print(nums) 

# extend() --> This method is used to add multiple items to a list at the end,
# where each element (or character in a string) is added as a separate item.

# remove() --> This method is used to remove a specific element from a list.
# It removes only the first occurrence of the given value.

a = [1, 2, 3, 2]

a.remove(2)
a.remove(2)
print(a)
'''

# pop() --> This method is used to remove an element from a list using its index.
# If no index is given, it removes the last element.

a = [1, 2, 3, 9, 10]

a.pop(3)

print(a)

