'''
import My_module

print(My_module.add(5, 3))
print(My_module.name)

#GENERATORS
-----------

---> This is special type of functions that return as ITERATOR which one at time
--->A generator is a function that returns values one by one using yield instead of return.

It does not store all values in memory
It generates values on demand (lazy evaluation)

#YIELD
-------
yield will take a pause and again resume, this is not a normal keyword can nothing be used in a normal functions
---> This is used to produce a value and pause execution.

#NEXT
------
---> This is used to get next value from a generator
---> When the value is finished, it will stop the iterator

def my_gen():
    yield 1
    yield 2
    yield 3

so = my_gen()
print(next(so))
print(next(so))
print(next(so)) 


def gen(n):
    for i in range(n):
        yield i*i

for val in gen(10):
    print(val)


#POWERS

def gen(n):
    for i in range(n):
        yield i**i

for value in gen(8):
    print(value)  


#

def gen(n):
    for j in range(n):
        yield i

for val in range(45):
    print(val)   '''


def even_gen(n):
    for i in range(4, n+1):
        if i % 2 == 0:
            yield i

for val in even_gen(100):
    print(val) 


