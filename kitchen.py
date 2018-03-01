for i in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	c,l=0,0
	for i in range(len(a)):
		l=a[i]-l
		if b[i]<=l:
			c+=1
		l=a[i]
	print(c)