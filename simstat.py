for i in range(int(input())):
	n,k = map(int,input().split())
	a=list(map(int,input().split()))
	a.sort()
	b=a[k:n-k]
	s=0
	for i in b:
		s+=i
	print("{:.6f}".format(s/(n-2*k)))

'''
def mx(k,a):
	if k==1:
		a.remove(max(a))
		return a
	return mx(1,mx(k-1,a))
def mn(k,a):
	if k==1:
		a.remove(min(a))
		return a
	return mn(1,mn(k-1,a))
for i in range(int(input())):
	n,k=map(int,input().split())
	a=list(map(int,input().split()))
	s=0
	if k==0:
		for i in range(n):
			s+=a[i]
		print("{:.6f}".format(s/n))
	else:
		mx(k,a)
		mn(k,a)
		for i in range(len(a)):
			s+=a[i]
		print("{:.6f}".format(s/len(a)))
'''