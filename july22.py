# num1 = 1
# num2 = 4
# num3 = 45
# if num1>num2:
#     print("Num1 is greater than num2")
# else:
#     print("Num2 is greather than num1")


# if num1>num2 and num1>num3:
#     print()
# else:
#     if num2>num1 and num2>num3:
#         print()
#     else:
#         print()



# print("Num1 is greather than Num2 and Num3" if num1>num2 and num1>num3 else "Num2 is greather than Num1 and Num3" if num2>num1 and num2>num3 else "Num3 is greather than Num1 and Num2")
# If body if condition true else else body



num = int(input("Enter a number: "))
# if num == 0:
#     print("Zero")
# elif num == 1:
#     print("One")
# elif num ==2:
#     print("Two")
# elif num == 3:
#     print("Three")
# elif num == 4:
#     print("Four")
# elif num == 5:
#     print("Five")
# else:
#     print("More than 6")


match num:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("More than 6")