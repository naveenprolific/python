def fib(num):
    if num ==0 :
        return 0
    elif num ==1:
        return 1
    else :
        result = fib(num-1)+fib(num-2)
        return result
fibvalue = int(input("enter the value to print the fib :"))
i=1
while  i < fibvalue :
    x = fib(i)
    print(x)
    i+=1
print("all done")
