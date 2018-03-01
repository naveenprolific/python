for i in range(int(input())):
	ls=int(input())
	n=list(map(int,input().split()))
	lf=int(input())
	f=list(map(int,input().split()))
	r=True
	for i in f:
		if i not in n:
			r=False
			break
	if r:
		print("Yes")
	else:
		print("No")

