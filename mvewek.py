for i in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	r=list(map(int,input().split()))
	p=[]
	for i in range(n):
		p.append(l[i]*r[i])
	ix,mx,rmx=0,0,0
	for i in range(len(p)):
		if p[i]>mx:
			mx=p[i]
			rmx=r[i]
			ix=i
		elif p[i]==mx and r[i]>rmx:
			mx=p[i]
			rmx=r[i]
			ix=i
	print(ix+1)