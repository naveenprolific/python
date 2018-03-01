
num1, oper, num2 = input("enter the calcualtion to do: ").split()
num1 = int(num1)
num2 = int(num2)
if oper is '+' :
      sumi  = num1+num2
      print("{} + {} = {}".format(num1,num2,sumi))
elif oper is '-' :
      diff = num1-num2
      print("{} - {} = {}".format(num1,num2,diff))
elif oper is '*' :
      mult = num1*num2
      print("{} * {} = {}".format(num1,num2,mult))
elif oper is '/' :
      div =  num1/num2
      print("{} / {} = {}".format(num1,num2,div))
elif oper is '%' :
      rem =  num1%num2
      print("{} % {} = {}".format(num1,num2,rem))
else:
    print("invalid operator...try again")
