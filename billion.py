for i in range(int(input())):
	n=int(input())
	s=input()
	c=input()
	w=list(map(int,input().split()))
	cnt=0
	for i in range(n):
		if s[i]==c[i]:
			cnt+=1
	if cnt==n:
		print(w[-1])
	else:
		print(max(w[:cnt+1]))
