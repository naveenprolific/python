for i in range(int(input())):
	b=int(input())
	if b>=1500:
		print("{}".format(b+500+(0.98*b)))
	else:
		print("{}".format(b+(0.1*b)+(0.9*b)))
