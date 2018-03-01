for i in range(int(input())):
	n,k=map(int,input().split())
	maxi=0
	for i in range(1,k+1):
		rem=n%i
		if maxi<=rem:
			maxi=rem
	print(maxi)
