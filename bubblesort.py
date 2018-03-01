arr=list(map(int,input("entr the elements :").split()))
def bubblesort(arr):
	for i in range(len(arr)):
		for k in range(len(arr)-1,i,-1):
			if(arr[k]<arr[k-1]):
				arr[k],arr[k-1]=arr[k-1],arr[k]
bubblesort(arr)
print(*arr,sep=" ,")


