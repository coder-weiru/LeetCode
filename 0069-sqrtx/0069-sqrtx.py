class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        num = 0
        for i in range(0, x + 1):
            if (i * i > x):
                num = i - 1
                break
            
        return num    