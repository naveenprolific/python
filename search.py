from array import *
lis = map(int,input("enter the elements :").split())
arr = array('i',lis)
l = int(input("enter the key to search for :"))
print("index of the key is :",arr.index(l))
for i in range(len(arr)):
	print(arr[i],end=' ')