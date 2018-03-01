class Empty(Exception):
    pass
class Arraystack:
    def __init__(self):
        self._data = []
    def is_empty(self):
        return len(self._data ) == 0
    def _len_(self):
        return len(self._data )
    def push(self):
        e = int(input("enter the element to push :"))
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Empty("stack  is empty")
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Empty("stack  is empty")
        return self._data.pop()
def switch_demo(choice):
    S = Arraystack()
    switcher = {1: S.push(),2: S.pop(),3:S.top(),4: S._len_(),5: S.is_mpty()}
    print(switcher.get(choice, "Invalid choice"))
def main():
    print("1->push\n2->pop\n3->top\n4->length\n5->isempty")
    ch = input("enter ur choice :")
    while True:
        switch_demo(ch)
main()
            
            
        
    
             
        
