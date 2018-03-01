n=int(input())
l=list(map(int,input().split()))
lucky,unlucky=0,0
for i in l:
	if i%2==0:
		lucky+=1
	if not(i%2==0):
		unlucky+=1
if lucky>unlucky:
	print("READY FOR BATTLE")
else:
	print("NOT READY")