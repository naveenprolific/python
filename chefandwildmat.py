for i in range(int(input())):
	 x=input()
	 y=input()
	 count=0
	 for i in range(len(x)):
	 	if x[i]!='?' and y[i]!='?' and x[i]!=y[i]:
	 		count+=1
	 if count!=0:
	 	print("No")
	 else:
	 	print("Yes")
	 		