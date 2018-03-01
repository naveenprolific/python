for i in range(int(input())):
	n,k=map(int,input().split())
	d=list(input().split())
	l=[]
	for i in range(k):
		x=input().split()
		l+=x
	r=[]
	for i in d:
		if i in l:
			r.append("YES")
		else:
			r.append("NO")
	print(*r)