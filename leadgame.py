a,b,w,l,m=0,0,0,0,0
for i in range(int(input())):
	s,t=map(int,input().split())
	a+=s
	b+=t
	l=abs(a-b)
	if l>m:
		m=l
		if (a-b)<0:
			w=2
		else:
			w=1
print(w,m)







