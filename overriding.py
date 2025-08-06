# class Parent:
#     def parent_method(self):
#         print("This is the parent method")

#     def eat(self):
#         print("I'm eating!!!")


# class Children(Parent):
#     def eat(self):
#         print("Running Eat Method")
#         super().eat()
#         return 3*12

# obj = Children()
# obj.eat()


# even = [i for i in range(1,11) if i %2 == 0]
# for i in range(1,11):
#     if i%2 == 0:
#         even.append(i)
# print(even)


# names = ["dad","mom","level","uday","nandini"]
# ans = [i for i in names if i == i[::-1]]
# print(ans)

# ans = []
# for i in names:
#     if i == i[::-1]:
#         ans.append(i)


# ans = [x for x in range(1,11)]
# print(ans)

# ans = {}
# for i in range(1,11):
#     ans[i] = i*i
# print(ans)


ans = {i:i*i for i in range(1,11) if i%2 ==0}
print(ans)