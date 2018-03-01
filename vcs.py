for i in range(int(input())):
	n,m,k=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	c1,c2=0,0
	for i in range(len(a)):
		for j in range(len(b)):
			if a[i]==b[j]:
				c1+=1
	a=set(a)
	b=set(b)
	x=a.union(b)
	x=list(x)
	for i in range(1,n+1):
		if i not in x:
			c2+=1
	print(c1,c2)

