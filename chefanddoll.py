from collections import Counter
for i in range(int(input())):
	n=int(input())
	l=[]
	for i in range(n):
		t=int(input())
		l.append(t)
	x=Counter(l)
	for i,j in x.items():
		if j!=2:
			print(i)
'''
def missing(dolls):
    for i in range(len(dolls)//2):
        if dolls[2*i] != dolls[2*i+1]:
            return dolls[2*i]
    return dolls[len(dolls)-1]
for i in range(int(input())):
    a = []
    n = int(input())
    for j in range(n):
        a.append(int(input()))
    print(missing(sorted(a)))