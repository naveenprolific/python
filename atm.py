atm=list(input().split())
t=int(atm[0])
b=float(atm[1])
if t%5==0 and (float(t)+0.5)<=b:
	bal=b-float(t)-0.50
	print("{:.2f}".format(bal))
else:
	print("{:.2f}".format(b))

