s=input()
for i in range(int(input())):
	w=input()
	f=False
	for i in w:
		if i not in s:
			f=True
	if(f):
		print("No")
	else:
		print("Yes")