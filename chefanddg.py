for i in range(int(input())):
	n=int(input())
	s=list(map(int,str(n)))
	if all([i==1 for i in s]) or all([i==0 for i in s]):
		print("NO")
	else:
		print("YES")