# n = 5
# for i in range(n):
#     print("*"*n)


# for i in range(1,6):
#     print("*",end="")
# print()
# for i in range(1,6):
#     print("*",end="")

# n = 6
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# n = 8
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

# n = 5
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# n = 10
# for i in range(n-1,-1,-1):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(1,(2*n-2*i)):
#         print("*",end="")
#     for j in range(i):
#         print(" ",end="")
#     print()

# n=4
# for i in range(1,n+1):
#     for j in range(i-1):
#         print(" ",end="")
#     for j in range(1,(2*n-2*i)+2):
#         print("*",end="")
#     for j in range(i-1):
#         print(" ",end="")
#     print()

# n = 4
# for i in range(n-1,-1,-1):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(1,(2*n-2*i)):
#         print("*",end="")
#     for j in range(i):
#         print(" ",end="")
#     print()
# for i in range(1,n+1):
#     for j in range(i-1):
#         print(" ",end="")
#     for j in range(1,(2*n-2*i)+2):
#         print("*",end="")
#     for j in range(i-1):
#         print(" ",end="")
#     print()


# n = 6
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()


# n = 5
# for i in range(1,2*n):
#     if(i<=n):
#         for j in range(i):
#             print("*",end="")
#     else:
#         for j in range(2*n-i):
#             print("*",end="")
#     print()


n = 5
for i in range(1,n+1):
    start = 1 if i%2 == 1 else 0
    for j in range(i):
        print(start,end="")
        start = 1-start
    print()