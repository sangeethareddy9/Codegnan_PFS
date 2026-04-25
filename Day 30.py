'''
File Handling ---> File handling is a process used to work with files.
A file handler is an object used to perform operations such as:
creating, reading, writing, updating and deleting the file.

How to open a file
1. open() ---> The open() function takes 2 parameters:
   1) file name
   2) mode
---> After opening the file, we must close it using close() function.

2. with open() ---> Recommended method (automatically closes file)

Modes ("r","w","a","x","t")

1. "r" ---> read
---> To read the file we use this mode.
---> If the file does not exist, it throws an error.

file = open("dummy.txt","r")
print(file.read())
file.close()

2. "w" ---> write
---> Used to write data into the file.
---> It creates the file if it does not exist.
---> If file exists, it overwrites the data.

file = open("dummy.txt","w")
file.write("I'm learning python")
file.close()

3. "a" ---> append
---> Used to add data to the file without deleting existing data.
---> It creates the file if it does not exist.

file = open("dummy.txt","a")
file.write("This is line 4")
file.close()

4. "x" ---> create
---> Used to create a new file.
---> Gives error if file already exists.

file = open("newfile.txt","x")
file.write("New file created")
file.close()

5. "t" ---> text mode
---> Default mode in Python.
---> Used for text files (no need to specify explicitly).

Example using with open():0

with open("dummy.txt","r") as file:
    print(file.read())

'''
