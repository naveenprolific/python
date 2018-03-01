'''
for i in range(int(input())):
	n=int(input())
	a=list(map(int,str(n)))
	a.reverse()
	b=int(''.join(map(str,a)))
	if n==b:
		print("wins")
	else:
		print("losses")
'''
for i in range(int(input())):
	n=int(input())
	b=0
	num=n
	while num!=0:
		rem=num%10
		b=b*10+rem
		num=num//10
	if n==b:
		print("wins")
	else:
		print("losses")