'''
MULTILEVEL INHERITENCE
----------------------
---> Multilevel inheritance is a type of inheritance in which a class
is derived from a class that is already derived from another class. 


class Grandparent:
    def Show_Grandparent(self):
        print("I'm Grandparent")

class Parent(Grandparent):
    def Show_Parent(self):
        print("I'm Parent")

class Child(Parent):
    def Show_child(self):
        print("I'm Child")

San = Child()
San.Show_Grandparent()
San.Show_Parent()
San.Show_child()


class Mobile:
    def basic_features(self):
        print("Calling, Messaging, Internet")

class Smartphone(Mobile):
    def advanced_features(self):
        print("Apps, Camera, Touchscreen")

class FlagshipPhone(Smartphone):
    def smooth_running(self):
        print("High Performance: Smooth and Fast")

phone = FlagshipPhone()

phone.basic_features()
phone.advanced_features()
phone.smooth_running()

HIERARCHICAL
------------  
#Hierarchical inheritance is a type of inheritance in which one parent class is inherited by more than one child class.  

class Parent:
    def parent_(self):
        print("I am Parent")

class Child1(Parent):
    def child1(self):
        print("I am 1st child")

class Child2(Parent):
    def child2(self):
        print("I am 2nd child")

class Child3(Child1, Child2):
    def child3(self):
        print("I am the child")

san = Child3()

san.parent_()
san.child1()
san.child2()
san.child3()


HYBRID INHERITANCE
------------------
---> Hybrid Inheritance is a type of inheritance that combines two or more types of inheritance
(like multilevel, multiple, or hierarchical) in a single program.  '''

class Parent:
    def parent_(self):
        print("I am Parent")

class Child1(Parent):
    def child1(self):
        print("I am Child 1")

class Child2(Parent):
    def child2(self):
        print("I am Child 2")

class Child3(Child1, Child2):
    def child3(self):
        print("I am Child 3")

thing = Child3()

thing.parent_()
thing.child1()
thing.child2()
thing.child3()




