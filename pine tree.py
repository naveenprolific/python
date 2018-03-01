n =input("how tall is tree :")
n = int(n)
spaces = n-1
hashes = 1
stumpspace = n-1
while n!=0 :
   for i in range(spaces):
           print('',end="")
   for i in range(hashes):
           print('#',end="")
   print()              
   spaces -= 1
   hashes +=2
   n -=1
for i in range(stumpspace):
    print('',end="")
print('#')    
   
