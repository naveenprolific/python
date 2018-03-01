from math import sqrt as s
def jumpsearch(arr,x,n):
	step = s(n)
	prev=0
	while arr[int(min(step,n)-1)]<x:
		prev = step
		step+=s(n)
		if prev>=n:
			return -1
	while arr[int(prev)]<x:
		prev+=1
		if prev==min(step,n):
			return -1
	if arr[int(prev)]==x:
		return prev
	return -1
arr = list(map(int,input("enter the array elements here<--' ").split()))
n= len(arr)
x = int(input("enter the number to find the index of ?"))
index = jumpsearch(arr,x,n)
print("Number" , x, "is at index",index)

