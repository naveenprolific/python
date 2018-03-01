for i in range(int(input())):
	n,b,m=map(int,input().split())
	t=0
	p=0
	while n!=0:
		p+=((n+1)//2)*m*(2**t)
		n-=(n+1)//2
		t+=1
	p+=(t-1)*b
	print(p)