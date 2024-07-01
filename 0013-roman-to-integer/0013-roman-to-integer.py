class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        deq = deque()
        for c in s:
            if deq:
                a = deq.pop()
                b = a + c
                if map.get(b):
                    deq.append(b)
                else:
                    deq.append(a)
                    deq.append(c)
            else:
                deq.append(c)
                
        #print(f"DEQ -> {deq}")
        
        val = 0
        while deq:
            n = deq.popleft()
            val += map[n]
            
        #print(f"Integer value: {val}");
        
        return val
                
        