# import sys
# nums = []
# firstSmall = nums[0]
# secondSmall = nums[0]
# for i in nums:
#     if i<firstSmall:
#         firstSmall = i

# for i in nums:
#     if i< secondSmall and i!=firstSmall:
#         secondSmall = i

for i in range(5):
    for j in range(4):
        if i == 0 or i == 4 or j == 0 or j == 3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

