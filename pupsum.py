def sum(d,n):
	if d==1:
		return n*(n+1)//2
	return sum(1,sum(d-1,n))
for i in range(int(input())):
	d,n=map(int,input().split())
	print(sum(d,n))

