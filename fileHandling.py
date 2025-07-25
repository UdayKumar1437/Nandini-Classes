# f = open("myFile.txt","r")
# content = f.read()
# print(content)


# f = open("myFile.txt","w")
# f.write("Uday Kumar 123")
# f.close()


# f = open("myFile.txt","a")
# f.write("Nandini")
# f.close()

# with open("myFile.txt","r") as f:
#     content = f.read()
#     print(content)

# f = open("myFile.txt","r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# for i in range(5):
#     line = f.readline()
#     print(line)


# f = open("myFile.txt","w")
# lines = ["uday \n","nandini \n","nitya \n"]
# f.writelines(lines)

# f = open("myFile.txt","w")
# lines = ["uday","kumar","nandini","nitya","kedar"]
# for i in lines:
#     f.write(i+" \n")
# f.close()


# with open("myFile.txt","r") as f:
#     f.seek(5) # Move to the 3rd byte of the file
#     data = f.read(5) # read the next 5 bytes
#     print(data)


with open("myFile.txt","r") as f:
    data = f.seek(2)
    print(data)

    curr_cursor = f.tell()
    print(curr_cursor)
