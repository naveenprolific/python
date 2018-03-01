for i in range(int(input())):
	p=bin(int(input()))[2:]
	if len(p)>=12:
		res=int(p[:-12]+'0',2)
		#print(res)
		p=p[-12:]
		#print(p)
	else:
		res=0
	for j in p:
		if j=='1':
			res+=1
	print(res)