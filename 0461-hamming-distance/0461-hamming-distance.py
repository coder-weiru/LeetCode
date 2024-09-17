class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = "{0:b}".format(x)
        b = "{0:b}".format(y)
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        d = 0
        for i in range(0, n):
            if int(a[i]) ^ int(b[i]) == 1:
                d += 1
                
        return d