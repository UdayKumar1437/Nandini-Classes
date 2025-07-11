# for i in range(1,11):
#     print("Nandini",i)

# num = 10
# for i in range(1,num+1):
#     if num%i ==0:
#         print(i)


# num = 7
# count = 0
# for i in range(2,num):
#     if num%i == 0:
#         count +=1
# if count == 0:
#     print("Prime")
# else:
#     print("Not Prime")


# name = "nandini sunkara"
# count = 0
# for i in name:
#     if i in "aeiouAEIOU":
#         count+=1

# print(count)


# num =23
# sum = 0
# for i in range(1,num+1):
#     sum += i
# print(sum)


# num = 123
# sum = 0
# for i in str(num):
#     sum+= int(i)
# print(sum)


# num = 371
# strNum = str(num)
# sum = 0
# l = len(strNum)
# for i in strNum:
#     sum+=int(i)**l
# if sum == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong number")


# num = 12
# sum = 0
# for i in range(1,num):
#     if num%i ==0:
#         sum +=i
# if sum>num:
#     print("Abudant Number")
# else:
#     print("Not an Abudant Number")


# print(ord(" "))

# name = "nanDiNi"
# ans = ""
# for i in name:
#     if i.isupper():
#         ans+=i.lower()
#     elif i.islower():
#         ans+=i.upper()
#     else:
#         ans+=i
# print(ans)


# name = "nandini"
# ans = ""
# for i in name:
#     if i not in "aeiouAEIOU":
#         ans +=i
# print(ans)

# name = "Nand23ini@!"
# ans = ""
# for i in name:
#     if i.isalpha():
#         ans+=i
# print(ans)

# name = "Nandi ni"
# ans = ""
# for i in name:
#     if ord(i) != 32:
#         ans+=i
# print(ans)


# a = "Nan123dini6"
# ans = 0
# for i in a:
#     if i.isdigit():
#         ans+=int(i)
# print(ans)


# num = 21
# sum = 0
# for i in str(num):
#     sum+=int(i)
# if num%sum == 0:
#     print("harshad")
# else:
#     print('Not a Harshad')

# num = 10
# for i in range(1,num+1):
#     if num%i == 0:
#         count = 0
#         for j in range(1,i+1):
#             if i%j ==0:
#                 count+=1
#         if count ==2:
#             print(i)


name = "Nandini"
ans = ""
for i in range(len(name)-1,-1,-1):
    ans=ans+name[i]
print(ans)

