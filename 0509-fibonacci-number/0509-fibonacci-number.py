class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        fib = {}
        fib[0] = 0
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
            
            #print(f"fib[{i}] -> {fib[i]}")
            
        return fib[n]    