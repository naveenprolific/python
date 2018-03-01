def multdiv(num1,num2):
    return  (num1*num2),(num1/num2)

def  isprime(num):
    for i in range(2,num):
        if(num%i)==0:
            return False
    return True
def getprimes(maxnum):
    listofp = []
    for i in range(2,maxnum):
        if isprime(i):
            listofp.append(i)
    return listofp

mult,div = multdiv(5,4)
print(mult,div)

maxnum = int(input("enter the number to search "))
listofprimes = getprimes(maxnum)
for i in listofprimes :
    print(i)


