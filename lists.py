import random
import math

rand = random.randrange(1,10)
newlist = list(range(rand))
for i in newlist :
    print("{} :{} ".format(newlist.index(i),i))

print("===============================")

mylist = []
for j in range(5):
    mylist.append(random.randrange(1,8))
for j in mylist :
    print("{} :  {} ".format(mylist.index(j),j))

