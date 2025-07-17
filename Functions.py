def names():
    print("Uday")
    print("Kumar")
    print("Nandini")

# names()
# names()


# A Function is a block of code that performs a specific task whenever is called.
# Two Types of functions
# Built- In Functions
# User Defined Functions



# def function_name(parameters):
#     pass
#     # Code here

# def add(num1,num2):
#     print(num1+num2)

# add(1,2)


# def add(num1,num2):
#     return num1+num2

# ans = add(1,2)



# Function Arguements
# Default Arguement
# We can provide a default value while clreating a function.
# def add(num1,num2=20,num3=10):
#     print(num1+num2+num3)

# add(1,3)


#  Keyword Argument
# We can provide arguements with key = value pairs , this way interpretor recognizes the arguements by the parameters name.

# def name(fname,mname,lname):
#     print("hello",fname,mname,lname)

# name(lname="Valapudasu",fname="Uday",mname="Kumar")


# Required Arguement
# def name(fname):
#     print(fname)

# name()


# Variable Length Arguements

# def names(*name):
#     for i in name:
#         print(i)

# names("Nandini","kedar","Uday","Nitya","Kundan")

# def add(*nums):
#     sum = 0
#     for i in nums:
#         sum+=i
#     print(sum)
# add(1,2,3,4,5,6)


# KeyWord Arbitrary arguement
# def name(**names):
#     print(names)

# name(name="uday",fname="Valapudasu")



# start = 2
# end = 10

# def isPrime(num):
#     count = 0
#     for i in range(2,num):
#         if num%i == 0:
#             count+=1
#     return count == 0

# for i in range(start,end+1):
#     if isPrime(i):
#         print(i)


def isArmstrong(num):
    sum = 0
    for i in str(num):
        sum+=int(i)**len(str(num))
    return sum == num

for i isetsn range(1,500):
    if isArmstrong(i):
        print(i)