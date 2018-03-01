import math
for i in range(int(input())):
	n,q=map(int,input().split())
	d=list(map(int,input().split()))
	x=list(map(int,input().split()))
	for i in range(q):
		for j in range(n):
			x[i] = math.floor(x[i]/d[j])
	print(*x)

'''t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s=1
    for j in a:
        if s<=1000000000:
            s=s*j
    for j in b:
        if j<s:
            print(0,end=" ")
        else:
            print(int(j/s),end=" ")
    print() 
    '''


