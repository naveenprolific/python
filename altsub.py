for i in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	l=[1]*n
	for i in reversed(range(1,n)):
		if a[i]*a[i-1]<0:
			l[i-1]=l[i]+1
	print(*l)