n=int(input())
p1=0
p2=0
bestlead=0
for i in range(1,n+1):
	inp = input()
	p1+=int(inp.split(' ')[0])
	p2+=int(inp.split(' ')[1])
	print(p1)
	print(p2)
    
	if abs(bestlead) < abs(p1-p2):
		bestlead=p1-p2
 
 
if bestlead > 0:
	print('1 ',abs(bestlead))
else:
	print('2 ',abs(bestlead))