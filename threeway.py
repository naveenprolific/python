
for i in range(int(input())):
	r=int(input())
	count=0
	x1,y1=map(int,input().split())
	x2,y2=map(int,input().split())
	x3,y3=map(int,input().split())
	if pow((x1-x2),2)+pow((y1-y2),2)<=r*r:
		count+=1
	if pow((x2-x3),2)+pow((y2-y3),2)<=r*r:
		count+=1
	if pow((x1-x3),2)+pow((y1-y3),2)<=r*r:
		count+=1
	if count>1:
		print("yes")
	else:
		print("no")
