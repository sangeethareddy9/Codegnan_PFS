'''
POLYMORPHISM
-------------
---> Polymorphism means “one name, many forms.”

---> It allows objects of different classes to be treated as objects of a common base class,
with the same method behaving differently depending on the object type.

EXAMPLE:-
--------
print(len("Python"))
print(len([1, 2, 3]))

METHOD OVERLOADING
------------------

---> Method overloading is a feature of Object-Oriented Programming where multiple methods
have the same name but different parameters (number, type, or order of parameters).

---> It is an example of compile-time polymorphism. 
#EXAMPLE1
class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c



obj = Calculator()
print(obj.add(2))        #2
print(obj.add(2, 3))     #5  
print(obj.add(2, 3, 4))  #9             

#EXAMPLE2
class Calculator:

    def add(self, a, b=0):
        return a + b


obj = Calculator()

print(obj.add(5))      # 5
print(obj.add(5, 3))   # 8

class Calculator:

    def sub(self, a, b=0, c=0):
        return a - b - c


obj = Calculator()

print(obj.sub(5))        # 5
print(obj.sub(5, 2))     # 3
print(obj.sub(5, 2, 1))  # 2


METHOD OVERRIDING
__________________

---> This occurs in the child class where a parent class method is redefined with the same name
and parameters (same signature) to achieve runtime polymorphism.


class animal:
    def speak(self):
        return "Sound"

class dog(animal):
    def speak(self):
        return "Bow Bow"

DOG = dog()
print(DOG.speak())   


class animal:
    def speak(self):
        return "sound"

class cat(animal):
    def speak(self):
        return "Meow Meow"

CAT = cat()
print(CAT.speak())  


class Instrument:
    def play(self):
        print("Instrument is playing")


class Guitar(Instrument):
    def play(self):
        print("Guitar is playing")


class Violin(Instrument):
    def play(self):
        print("Violin is playing")

g = Guitar()
v = Violin()

g.play()
v.play()

OPERATOR OVERLOADING
--------------------
-->This is customizes operator like +, - for user-defined classes by implementing special methods...

#EXAMPLE __add__, __sub__ 
--------


class someone:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self,other):
        return someone(self.a +other.a, self.b + other.b)
    def __str__(self):
        return f"({self.a}, {self.b})"
any = someone(2,3)
so = someone(5,9)
print(any + so) 


DATA ABSTRACTION
----------------
---> This hides complex implementation details, exposing only essential features via abstract class or interface  '''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2



obj = Circle(5)
print(obj.area())
















