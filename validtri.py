for i in range(int(input())):
	x,y,z=map(int,input().split())
	if x>0 and y>0 and z>0 and(x+y+z==180):
		print("YES")
	else:
		print("NO")