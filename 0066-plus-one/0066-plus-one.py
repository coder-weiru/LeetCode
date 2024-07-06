class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 > 9:
                digits[i] = 0
                r = 1
            else:
                digits[i] += 1
                r = 0
                break

        if r > 0:
            digits.insert(0, 1)

        #print(f"list -> {digits}")    
        
        return digits    
