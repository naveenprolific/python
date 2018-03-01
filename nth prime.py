def prime(n):
    primes = 1
    num = 2
    while primes <= n:
            mod = 1
            ptrue = True
            while mod <= (num - 1):
                    if num%(num-mod) == 0:
                            ptrue = False
                            break
                    mod += 1
            if ptrue == True:
                    primes += 1
    return(primes)
q = int(input("enter the value of n :"))
print (prime(q))
