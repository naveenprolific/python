def count(arr,x):
	res=0
	for i in range(len(arr)):
		if x==arr[i]:
			res+=1
	return res
arr=list(map(int,input("enter the elements : ").split()))
x=int(input("enter the number to check :"))
print(count(arr,x))