from math import gcd
for i in range(int(input())):
	arr=list(map(int,input().split()))
	n=arr[0]
	res=arr[1]
	for i in arr[1:]:
		res=gcd(i,res)
	print(*[i//res for i in arr[1:]])

	
'''
from math import gcd
t = int(input())
for ti in range(t):
    arr = [int(i) for i in input().split()]
    n = arr[0]
    arr0 = arr[1::]
    if n >= 2:
        c = gcd(arr0[0], arr0[1])
        for ni in range(2, n):
            c = gcd(c, arr0[ni])
        #print(c)
        a = [i//c for i in arr0]
        print(*a)
    else:
        print("1") 
        '''