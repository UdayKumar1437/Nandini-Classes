# Constructors

'''
A constructor is a special method in a class used to create and initilaize an object of a class.
A constructor will be called/invoked automatically when an object is created.
They are two types of constructors are available one is Parameterized constructor and default.
'''


# Default Constructor --> It doesn't accept any arguements
# class Person:

#     def __init__(self):
#         print(f"I'm a default Construtor")
#     def getName(self):
#         print(f"My Name is Nandini")

# obj = Person()
# obj1 = Person()
# obj.getName()


#Parameterized Constructor --> It accepts parameters

class Details:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def getName(self):
        print(f"My Name is {self.name}")
    def getAge(self):
        print(f"I'm {self.age} years old")

obj1 = Details("Nandini",19)
obj2 = Details("Uday",25)
obj1.getAge()
obj2.getAge()

