for i in range(int(input())):
	n=int(input())
	s=list(map(str,str(input())))
	r=s.count('R')
	b=s.count('B')
	g=s.count('G')
	print(n-max(r,g,b))
