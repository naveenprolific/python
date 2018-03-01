import os

with open("mydata.txt",mode="w",encoding = "utf-8") as myfile :
    myfile.write("some random text \nhello")
with open("mydata.txt",encoding = "utf-8") as myfile:
    print(myfile.read())
    print(myfile.readline())
    print(myfile.readlines())
