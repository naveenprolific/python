arr=list(map(int,input("enter the elements of sequence").split()))
x=list(set(arr))
l=[]
for i in range(len(x)):
	l.append(arr.count(x[i]))
print(l)
print("max plateau is of length :",max(l))