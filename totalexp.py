for i in range(int(input())):
	q,p=map(int,input().split())
	if q>1000:
		c=(q*p)-(q*p)*0.1
		print("{:.6f}".format(c))
	else:
		c=q*p
		print("{:.6f}".format(c))
