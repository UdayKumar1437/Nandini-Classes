# class Student:
#     isStudying = True
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# obj = Student("Nandini",19)
# print(obj.age)
# print(obj.name)

# class Student:
#     def __init__(self,name,age):
#         self.__age = age

#         def __name(self):
#             self.check = age
#             print(self.check)
#     def getAge(self):
#         print(self.__age)

# class Subject(Student):
#     pass

# obj = Student("Uday",25)
# obj1 = Subject("Nandini",19)
# # print(obj.getAge())

# print(obj1.__age)


class Student:
    def __init__(self,name,age):
        self._name = name
        self.__age = age

    def _funName(self):
        print(self._name)

class Nandini(Student):
    def getName(self):
        print(self._name)

obj = Nandini("Nandini Sunkara",19)
obj.getName()
obj._funName()
print(obj._name)