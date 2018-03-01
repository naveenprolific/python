from math import gcd
def lcm(a,b):
	return a*b//gcd(a,b)

for i in range(int(input())):
	a,b=map(int,input().split())
	print(gcd(a,b),lcm(a,b))