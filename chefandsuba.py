for i in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	c=0
	for j in range(n):
		s,p=0,1
		for k in range(j,n):
			s+=a[k]
			p*=a[k]
			if s==p:
				c+=1
	print(c)
