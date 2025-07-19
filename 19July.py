# arr = [1,1,2,5,3,5,5,2,1,2,3,1,10]

# ans = {}


# for i in arr:
#     if i not in ans.keys():
#         ans[i] = 1
#     else:
#         ans[i] = ans[i]+1
# for i in ans:
#     if ans[i] == 1:
#         print(i)


# ans = {
#     "odd":0,
#     "even":0
# }

# for i in arr:
#     if i%2==0:
#         ans["even"] = ans["even"]+1
#     else:
#         ans["odd"] += 1
# print(ans)



# s = "nandini Sunkara is a good girl"
# arr = s.split(" ")
# # print(arr[0])
# arr[0] = arr[0].capitalize()
# arr[-1] = arr[-1].capitalize()
# ans = " ".join(arr)
# print(ans)


# num = 205
# count = 0
# while num>0:
#     # lastD = num%10
#     count +=1
#     num = num//10
# # for i in str(num):
# #     count+=1
# print(count)



arr = [1,2,3,6,5,8,9,40]

ans = [x for x in arr if x%3==0]
# for i in arr:
#     if i%3==0:
#         ans.append(i)

print(ans)