def func(num):
    
        if num%2==0:
            return False
        else :
            return True
def lf(l,func):
    ol =[]
    for i in range(len(l)):
         if func(i):
             ol.append(i)
    return ol
       
def main():
    l = [1,2,3,4,5,6]
    print(lf(l,func))

main()
