for i in range(int(input())):
	n,k=map(int,input().split())
	c=0
	for i in range(n):
		t,d=map(int,input().split())
		if k>0:
			if t>=k:
				t-=k
				k=0
			else:
				k-=t
				t=0
		c+=t*d
	print(c)
