from collections import Counter
arr=Counter(list(map(int,input("enter the sequence -->").split())))
for k,v in arr.items():
	print(k,"-->",v," times")
