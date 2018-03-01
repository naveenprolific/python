for i in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	r=[1]*len(a)
	for i in range(1,len(a)):
		if a[i]>=a[i-1]:
			r[i]=r[i-1]+1
	print(sum(r))
