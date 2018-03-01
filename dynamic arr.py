import ctypes

class dynamic_array:
    def __init__(self):
        self._n=0
        self._capacity=1
        self._A = self._make_array(self._capacity)
    def _len_(self):
        return self._n
    def  getitem(self,k):
        if not 0<= k <=self._n:
            raise IndexError("invalid index")
        return self._A[k]
    def _append(self,obj):
        if self._n == self._capacity:
            self.resize(2* self._capacity)
        self._A[self._n]= obj
        self._n += 1
        
    def resize(self,c):
        B = self.__make_array(c)
        for i in range(sel._n):
            B[i]=self._A[i]
        self._A = B
        self._capacity=c
    def _make_array(self,c):
        return (c*ctypes.py_object)()
def main():
    A = dynamic_array()
    print(A)
main()
    
