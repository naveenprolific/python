for i in range(int(input())):
	x1,y1,x2,y2=map(int,input().split())
	if x1==x2:
		if y1>y2:
			print("down")
		elif y1<y2:
			print("up")
	elif y1==y2:
		if x1>x2:
			print("left")
		elif x1<x2:
			print("right")
	else:
		print("sad")