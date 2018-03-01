class Fibonacci:

    def __init__(self, k):
        self.cache = []
        self.k = k

        #Bootstrap the cache
        self.cache.append(1)
        for i in range(1,k+1):
            self.cache.append(1 << (i-1))

    def fib(self, n):
        #Extend cache until it includes value for n.
        #(If we've already computed a value for n, we won't loop at all.)
        for i in range(len(self.cache), n+1):
            self.cache.append(2 * self.cache[i-1] - self.cache[i-self.k-1])

        return self.cache[n]

if __name__ == '__main__':
    k = 5
    f = Fibonacci(k)
    for i in range(10):
        print(f.fib(i))