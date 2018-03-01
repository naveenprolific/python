def f(s):
	b,mb=0,0
	for i in range(len(s)):
		if s[i]=='(':
			b+=1
		if s[i]==')':
			b-=1
		mb=max(mb,b)
	return mb
for i in range(int(input())):
	a=input()
	print("("*f(a)+")"*f(a))
