for i in range(int(input())):
	s1=input()
	s2=input()
	mini,maxi=0,0
	for i in range(len(s1)):
		if s1[i]!='?' and s2[i]!='?' and s1[i]!=s2[i]:
			mini+=1
			maxi+=1
		elif s1[i]=='?' or s2[i]=='?':
			maxi+=1
	print(mini,maxi)