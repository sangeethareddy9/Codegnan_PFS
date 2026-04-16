'''
#OOP'S
-------

Introduction to oop's
1)Classes
2)Object
3)attributes
4)Methods

OOP's
------

---> Object Oriented Programming (OOP) is a style of programming 
     where we model real-world things as objects that contain 
     both data and functions.

---> Class is a blueprint or template that defines what kind 
     of data and behaviour an object will have.


Object
-------

---> An object is an instance of a class.

---> It is a real entity created from a class and exists 
     in memory while the program is running.

Attributes
----------
Attributes are variables inside a class.
They store the data of an object.             

example-
---------

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        

c1 = Car("BMW", "black")
c2 = Car("Audi", "white")

print(c1.brand)
print(c2.brand)


class Lion:
    def __init__(self, name, age):
        self.name = name   
        self.age = age     


l1 = Lion("Simba", 4)
l2 = Lion("Leo", 6)

print(l1.name, l1.age)
print(l2.name, l2.age)  '''


class car:
    wheels = 4
    def __init__(self, male, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 20
    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} Miles. Total: {self.mileage}"
    def info(self):
        return f"{self.make} {self.model} {self.year}"
car_1 = car(make = "Ford", model: "Mustang", year: "2008")
car_2 = car(make ="Toyoto", model: "camry", year: "2023")
    
    

