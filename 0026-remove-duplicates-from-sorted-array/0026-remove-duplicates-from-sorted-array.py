class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map = {}
        m = len(nums)
        for i in range(1, m):
            if nums[i] == nums[i - 1]:
                map[i] = nums[i]
            
        #print(f" map -> {map}")
        
        for v in map.values():   
            nums.remove(v)
            nums.append(v)
                
        #print(f" nums ... -> {nums}")

        return m - len(map)