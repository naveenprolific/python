def linsearch(arr,x):
	for i in range(len(arr)):
		if arr[i]==x:
			return i
	return -1
'''
if x in arr:
	print(arr.index(x))
'''
print(linsearch([int(input()) for i in range(int(input("enter the size of array :")))],int(input("enter the key to serach for? "))))
