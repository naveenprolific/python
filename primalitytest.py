def isprime(n):
	if(n>1):
		div=2
		for i in range(div,n):
			if n%i==0:
				return False
	else:
		return False
	return True
	
for i in range(int(input())):
	n=int(input())
	if(isprime(n)):
		print("yes")
	else:
		print("no")
