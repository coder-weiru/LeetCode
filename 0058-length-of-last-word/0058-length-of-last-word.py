class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1 
        j = -1
        b = False
        for n in range(len(s) -1, -1, -1):
            if s[n] is not ' ' and b is False:
                i = n
                b = True
            if s[n] is ' ' and b is True:
                j = n
                break
        return i - j