for i in range(int(input())):
	n,k=map(int,input().split())
	g=list(map(int,input().split()))
	c=0
	for i in g:
		if i<k:
			c+=k-i
			#print(c)
		else:
			r=i%k
			c+=min(r,k-r)
			#print(min(r,k-r))
			#print(c)
	print(c)
