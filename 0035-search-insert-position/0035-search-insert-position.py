class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            elif nums[0] > target:
                return 0
            elif nums[0] < target:
                return 1
            
        elif n > 1:    
            
            mid = int(n / 2)
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                
                #print(f"mid: {mid}, nums: {nums}")
                
                return self.searchInsert(nums[:mid], target)
            
            elif nums[mid] < target:    
            
                #print(f"mid: {mid}, nums: {nums}")
                
                return mid + self.searchInsert(nums[mid:], target)