class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(c for c in s if c.isalnum()).lower()
        
        l = len(a)
        for i in range(l):
            
            if l - i - 1 < i:
                break
            
            #print(f"a[{i}] -> {a[i]}, a[{l - i - 1}] -> {a[l - i - 1]}")
                
            if a[i] is not a[l - i - 1]:
                return False
            
                
        return True
                