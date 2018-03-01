'''for i in range(int(input())):
	arr=list(map(int,str(int(input()))))
	print(arr[0]+arr[-1])
	'''
t=int(input())
j,count=0,0
l=[]
for i in range(t):
	n=int(input())
	while n!=0:
		d=n%10
		l.append(d)
		n=n//10
	count=l[0]+l[-1]
	#print(l)
	print(count)





		
	