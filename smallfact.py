def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)
for i in range(int(input())):
	num=int(input())
	print(fact(num))