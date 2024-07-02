class Solution:
    def isclosed(self, a: str, b: str) -> bool:
        map = {
        '(': 1,
        ')': -1,
        '[': 2,
        ']': -2,
        '{': 3,
        '}': -3
        }
        return map[a] + map[b] == 0 and map[a] > map[b]
        
    
    def isValid(self, s: str) -> bool:
        n = len(s) 
        if n % 2 > 0:
            return False
        
        deq = deque()
        for c in s:
            if deq:
                prev = deq[-1]
                
                #print(f"deq : {deq}, prev: '{prev}', c: '{c}'")
                
                if self.isclosed(prev, c):
                    deq.pop()
                else:    
                    deq.append(c)
            else:
                deq.append(c)
            
        return len(deq) == 0 
            
            