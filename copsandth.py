for i in range(int(input())):
	m,x,y=map(int,input().split())
	n=list(map(int,input().split()))
	t=x*y
	n.append(100+t+1)
	#print(n)
	n.sort()
	#print(n)
	p=0
	h=0
	for i in n:
		if i-t-1>p:
			h+=i-t-1-p
		p=i+t
		#print(p)
	print(h)



