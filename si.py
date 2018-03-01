invam,intrst = input("enter a investment and intrst rate :").split()
invam = float(invam)
intrst = float(intrst)* 0.01
for years in range(11) :
        invam = invam + (invam*intrst)
savings = invam 
print("earnings  after 10 years : {:.2f}".format(savings))
