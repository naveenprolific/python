for i in range(int(input())):
	g=int(input())
	l=input()
	if 'I' in l:
		print("INDIAN")
	elif 'Y' not in l:
		print("NOT SURE")
	else:
		print("NOT INDIAN")