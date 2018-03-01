class fib:
    def __init__(self):
        self.first = 0
        self.second =1
        
    def __iter__(self):
        return self
    def __next__(self):
        fibnum = self.first + self.second
        self.first = self.second
        self.second = fibnum
        return fibnum
            
def main():
    fibseq = fib()
    n = int(input("enter the number of terms :"))
    for i in range(n):
        print("fib :",next(fibseq))
main()
