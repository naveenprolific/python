for i in range(int(input())):
	arr=list(map(int,str(int(input()))))
	arr.reverse()
	print(int(''.join(map(str,arr))))