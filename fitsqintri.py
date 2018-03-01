def num(b):
	count=0
	if b==1:
		return 0
	while b>1:
		count+=(b-2)//2
		b=b-2
	return count

for i in range(int(input())):
	b=int(input())
	print(num(b))
