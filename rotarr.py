from array import *
lis = map(int,input("enter the elements :").split())
arr = array('i',lis)
l = int(input("enter the width to rotate :"))
arr = arr[l:]+arr[:l]
for i in range(len(arr)):
	print(arr[i],end=' ')