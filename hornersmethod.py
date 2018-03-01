def horner(poly,x):
	res = poly[0]
	for i in range(1,len(poly)):
		res=res*x+poly[i]
	return res
poly=list(map(int,input("enter the elements of polynomial -->").split()))
x=int(input("enter the value of x : "))
print("value of polynomial is :",horner(poly,x))