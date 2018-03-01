n=int(input("enter the range :"))
armst =[]
for i in range(n):
	sum=0
	temp=i
	while temp>0:
		digit=temp%10
		sum  += digit**3
		temp//=10
	if sum ==i:
		armst.append(i)
print(*armst,sep=" ,")

    

	
	





