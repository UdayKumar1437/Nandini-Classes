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


num = 12
sum = 0
for i in range(1,num):
    if num%i ==0:
        sum +=i
if sum>num:
    print("Abudant Number")
else:
    print("Not an Abudant Number")