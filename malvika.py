for i in range(int(input())):
	s=list(map(str,input()))
	c1=s.count('a')
	c2=s.count('b')
	print(min(c1,c2))
