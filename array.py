from array import *
arr = array('i',[1,2,3,3])

arr.append(7)
arr.insert(2,6)
arr.remove(2)
arr.reverse()
for i in range(len(arr)):
	print(arr[i],end=" ")

print('\n',arr.index(6))