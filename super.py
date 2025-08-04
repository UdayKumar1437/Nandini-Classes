# Super keyword in python is used to refer the parent class

# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method")

# class ChildClass(ParentClass):
#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()
# childObj = ChildClass()
# childObj.child_method()



# class ParentClass1:
#     def parent_method(self):
#         print("This is the parent method from parent class 1")

# class ParentClass2:
#     def parent_method(self):
#         print("This is the parent method from parent class 2")

# class ChildClass(ParentClass1,ParentClass2):
#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()
# childObj = ChildClass()
# childObj.child_method()

# def ab():
#     print("ok")
# def x(y):
#     y()

# x(ab)


# nums = [1,2,3,4,5]

# def square(x):
#     return x*x

# ans = map(square,nums)
# print(list(ans))
# ans = []
# for i in nums:
#     ans.append(i**2)
# print(ans)



# nums = [1,2,3,5,8,9,4,6,75]

# def checkEven(num):
#     return num%2 == 0
# fil = filter(checkEven,nums)
# print(list(fil))


# A Lambda function is a small anonymous function without a name

# nums = [1,2,3,4,5]

# # def square(x):
# #     return x*x

# ans = map(lambda x : x*x,nums)
# print(list(ans))

def multiply(a,b):
    return a*b

ans = lambda a,b : a*b
print(ans(2,3))

