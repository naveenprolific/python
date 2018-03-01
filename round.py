invam,intrst = eval(input("enter a float...:")).split()
for years in range(11) :
        invam = invam + invam*intrst

print("round to 2 dec : {:.3f}".format(invam))
