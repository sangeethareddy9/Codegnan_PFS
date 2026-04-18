'''
Constructor(__init__)
----------------------
--->A constructor is a special method used to initialise object data __init__()

#example:- 

class student:
  def __init__ (self, name, ID):
    self.name = name
    self.ID = ID
  def display(self):
    print(self.name, self.ID)
Stu_1 = student("San", 909)
Stu_1.display()




class dog:
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color
dog_1 = dog("pomerian","orange")
dog_2 = dog("husky","white")
print(dog_1.breed,dog_1.color)



class lays:
    def __init__(self,f
     lavour,color):
        self.flavour = flavour
        self.color = color
lays_1 = lays("blue masala","blue")
lays_2 = lays("onion cream","green")
print(lays_1.flavour,lays_1.color)

syntax -- __name
#this is restricted one  '''

class some:
 def __init__(self):
   self.public = "public"
   self.protected = "protected"
   self.private = "private"
any = some()
print(any.__public)
print(any.protected)
print(any.private)
  



