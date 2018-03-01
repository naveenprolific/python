
for i in range(int(input())):
	t=[]
	for j in range(int(input())):
		t.append(input())
	s=set(t)
	if len(s)==1:
		print(t[0])
	else:
		s=list(s)
		c=0
		for i in t:
			if i==s[0]:
				c+=1
		if c==len(t)-c:
			print("Draw")
		elif c>len(t)-c:
			print(s[0])
		else:
			print(s[1])
    #if t.count(s[0])==t.count(s[1]):
			#print("Draw")
		#elif t.count(s[0]) > t.count(s[1]):
			##print(s[0])
		#else:
			#print(s[1])
