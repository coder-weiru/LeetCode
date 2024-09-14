class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        
        if j == 0:
            if nums[j] == val:
                return 0
            else:
                return 1
            
        while i <= j:
            a = nums[i]
            b = nums[j]
            if a == val and b != val:
                nums[i] = b
                nums[j] = a
            elif a == val and b == val:
                j -= 1
            else: 
                i += 1
        
        #print(f"k: {i}")
        #print(nums)
        return i       