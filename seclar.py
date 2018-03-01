for i in range(int(input())):
	a,b,c=map(int,input().split())
	if min(a,b,c)<a<max(a,b,c):
		print(a)
	elif min(a,b,c)<b<max(a,b,c):
		print(b)
	else:
		print(c)