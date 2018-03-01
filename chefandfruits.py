for i in range(int(input())):
	n,m,k=map(int,input().split())
	if k<=abs(n-m):
		print(abs(n-m)-k)
	else:
		print(0)
