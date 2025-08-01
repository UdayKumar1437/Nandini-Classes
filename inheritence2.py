# class BaseClass:
#     def uday(self):
#         print("Uday Kumar from baseclass")

# class Children:
#     def nandini(self):
#         print("Nandini Sunkara")
#     def uday(self):
#         print("Uday Kumar from chindren")

# class Children2(Children,BaseClass):

#     def uday(self):
#         print("Uday from child2 class")
#     def madhavi(self):
#         print("Madhavi Sunkara")

# obj = Children2()
# obj.uday()


# class BaseClass:
#     def uday(self):
#         print("Uday Kumar from baseclass")

# class Children(BaseClass):
#     def nandini(self):
#         print("Nandini Sunkara")
#     def uday(self):
#         print("Uday Kumar from chindren")

# class Children2(BaseClass):

#     # def uday(self):
#     #     print("Uday from child2 class")
#     def madhavi(self):
#         print("Madhavi Sunkara")

# obj = Children2()
# obj.uday()


class A:
    pass

class B(A):
    pass

class C:
    pass
class D(B,C):
    pass