class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while i < len(haystack):
            a = haystack[i]
            b = needle[j]
            
            if a == b:
                i += 1
                j += 1
                
                if j == len(needle):
                    break
            else:
                if j > 0:
                    i = i -j + 1
                    j = 0
                else:
                    i += 1
        
        if j < len(needle):
            return -1
        else:
            return i - len(needle)