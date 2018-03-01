for i in range(int(input())):
	h,c,t=map(float,input().split())
	if int(h)>50 and c<0.7 and int(t)>5600:
		print(10)
	elif int(h)>50 and c<0.7 :
		print(9)
	elif c<0.7 and int(t)>5600:
		print(8)
	elif int(h)>50  and int(t)>5600:
		print(7)
	elif int(h)>50 or c<0.7 or int(t)>5600:
		print(6)
	else:
		print(5)
