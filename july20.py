# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
# print("Completed")

# def uday():
#     pass


# a = float(input("Enter Number 1: "))
# b = int(input("Enter Number Two: "))
# # print(f"The user entered is {a}")
# # print(a+b)
# print(a)



# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1,num+1):
#     sum+=i
# print(sum)

try:
    arr = [1,2,3]
    # print(arr[10])
    print(arr[0])
except ZeroDivisionError:
    print("I catched the error")
except IndexError:
    print("Index Error caught")
else:
    print("Runs when there is no errors in our code")
finally:
    print("Monark")

# print(list(reversed([4,2,2])))
