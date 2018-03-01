
def solve(eq):
    x,add,num1,equal,num2 = eq.split()

    num1,num2 = int(num1),int(num2)
    
    return "x = "+str(num2 - num1)

print(solve("x + 4 = 9"))
   
