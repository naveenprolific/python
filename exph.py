import sys

try:
    myfile = open("mydata.txt",encoding ="utf-8")

except FileNotFoundError as ex:
    print("file is not found")
    print(ex.args)
else:
    print("file :",myfile.read())
    myfile.close()
finally :

    print("finished  working")
