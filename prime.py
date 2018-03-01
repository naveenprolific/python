for i in range(2,int(input("enter the n :"))):
	for x in range(2,i):
		if i%x==0:
			#print(i,'equals',x,'*',i//x)
			break
	else :
		print(i," is a prime")