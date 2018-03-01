def largestsum(tri):
	size=len(tri)
	for a in range(size-2,-1,-1):
		for b in range(0,len(tri[a])):
			if tri[a+1][b]>=tri[a+1][b+1]:
				tri[a][b]+=tri[a+1][b]
			else:
				tri[a][b]+=tri[a+1][b+1]
	return tri[0][0]

for i in range(int(input())):
	n=int(input())
	tri=[]
	for j in range(n):
		tri.append([int(a) for a in input().split()])
	print(largestsum(tri))
