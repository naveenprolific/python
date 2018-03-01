for i in range(int(input())):
	s=input()
	if s[0]==s[1]:
		print("NO")
	else:
		for i in range(len(s)-2):
			if s[i]!=s[i+2]:
				print("NO")
				break
		else:
			print("YES")