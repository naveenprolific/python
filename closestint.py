def mindiff(arr):
	if len(arr)<=1:return
	arr.sort()
	diff=arr[1]-arr[0]
	for i in range(2,len(arr)):
		diff=min(diff,arr[i]-arr[i-1])
	for i in range(1,len(arr)):
		if (arr[i]-arr[i-1])==diff:
			print("(",arr[i-1],",",arr[i],")")

arr=list(map(int,input("enter the sequence here:").split()))
mindiff(arr)

	


