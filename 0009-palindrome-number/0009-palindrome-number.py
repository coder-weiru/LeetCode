class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        l = len(a)
        for i in range(l):
            if a[i] != a[l - i - 1]:
                return False
        return True
        