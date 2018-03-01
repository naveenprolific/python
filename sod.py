for i in range(int(input())):
	n=int(input())
	sum=0
	while n!=0:
		rem=n%10
		sum+=rem
		n=n//10
	print(sum)