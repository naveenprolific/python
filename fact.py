for i in range(int(input())):
	count=0
	p=1
	n=int(input())
	while n>=5**p:
		count+=n//(5**p)
		p+=1
	print(count)