
for i in range(int(input())):
	n,m=map(int,input().split())
	c =[0]*2
	for j in range(n):
		s = input().strip()
		for k in range(0,len(s)):
			if s[k]=='R':
				if (k+j)%2==0:
					c[1]+=5
				else:
					c[0]+=5
			else:
				if (k+j)%2==0:
					c[0]+=3
				else:
					c[1]+=3
	print(min(c))





	