def useStack():
    stack = []
    choice = -1
    while choice != 7:
        print("1->push\n2->pop\n3->display\n4->length\n5->isempty\n6->top")
        choice = int(input("enter ur choice >>"))
        if choice == 1:
            item = input("enter the item u want to push :")
            stack.append(item)
        if choice == 2:
            if len(stack)==0:
                print("stack is empty")
            else:
                x = stack.pop()
                print("the element poped is {}".format(x))
        if choice == 3:
            if len(stack)==0:
                print("stack is empty")
            for i in range(len(stack)-1,-1,-1):
                print(stack[i])
        if choice == 4:
            print("lenth of stack is :",len(stack))
        if choice == 5:
            if len(stack)==0:
                print("stack is empty")
            else :
                print("stack is not empty")
        if choice == 6:
             if len(stack)==0:
                print("stack is empty")
             else:
                print("top element is :",stack[-1])
         
    

useStack()
    
