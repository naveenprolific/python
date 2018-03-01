week={'mon':0,'tue':1,'wed':2,'thu':3,'fri':4,'sat':5,'sun':6}
for i in range(int(input())):
	days,day=input().split()
	c=[4]*7
	x=week[day]
	e = int(days)%7
	for j in range(e):
		if x>6:
			x%=7
		c[x]+=1
		x+=1
	print(*c)





	