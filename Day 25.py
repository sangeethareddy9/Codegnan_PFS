'''#ENCAPSULATION
---------------

---> The principle of bunding data(Attributes) and methods that operate on that data into a single unit, which is a class


class BankAC:
    def __init__(self, balance):
        self.__balance = balance   

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAC(18000)
acc.deposit(3000)
print(acc.get_balance())   

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("San", "reddy")
x.printname()

#INHERITANCE
-------------   
---> This allows a child class(subclass) to acquire the attributes and methods of a parents class(base class) this is called Inheritance
1. Single Inheritace
--------------------
---> It is a type of inheritance in which one child class inherits the properties and methods from one parent class.
class parent:
    def show(self):
        print("This is parent class")

class child(parent):   # Inheriting from parent
    def display(self):
        print("This is child class")

obj = child()
obj.show()     
obj.display()  

2. Multiple Inheritance
-----------------------
---> Multiple Inheritance is a type of inheritance where one child class inherits properties and methods from more than one parent class.


3. Multi - level Inheritance

super method()
--------------
---> This is used to call methods of the parent class from the child class 

class parent:
    def display(self):
        print("This is parent method")

class child(parent):   
    def display(self):
        super().display()   
        print("This is child method")

obj = child()
obj.display()  

class Father:
    def skill_1(self):
        print("Father: Hard working")

class Mother:
    def skill_2(self):
        print("Mother: Cooking")

class Child(Father, Mother):   
    def all_skills(self):
        print("Child: Coding")

ANy = Child()
ANy.skill_1()
ANy.skill_2()
ANy.all_skills()    '''

class Sports:
    def play(self):
        print("Playing sports")

class Studies:
    def study(self):
        print("Studying subjects")

class Student(Sports, Studies):   
    def activities(self):
        print("Student manages both")

obj = Student()
obj.play()
obj.study()
obj.activities()   
      



