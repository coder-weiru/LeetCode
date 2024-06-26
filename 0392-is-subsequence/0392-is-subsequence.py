class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        sub = ''
        while i < len(s):
            while j < len(t):
                a = s[i]
                b = t[j]
                j += 1
                
                if a == b:
                    sub += a
                    break
        
            i += 1    
        
        return sub == s
        
                