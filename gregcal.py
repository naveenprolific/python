day=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
for i in range(int(input())):
	y=int(input())
	k=0
	y1=(y-1)//100
	if y1%4==3:
		k+=1
	if y1%4==2:
		k+=3
	if y1%4==1:
		k+=5
	if y1%4==0:
		k+=0
	y2=(y-1)%100
	k+=(y2+y2//4)%7
	print(day[(k+1)%7])

