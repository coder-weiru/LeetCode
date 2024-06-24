class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for n in range(len(s)):
            m = len(s) - n - 1
            a = s[n]
            s[n] = s[m]
            s[m] = a
            if (m - n <= 1):
                break
                    
                