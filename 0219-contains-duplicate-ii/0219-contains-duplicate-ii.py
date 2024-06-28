class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 0
        map = {}
        while r < len(nums):
            
            #print(f"l -> {l}, r -> {r}, nums[{r}] -> {nums[r]}, map -> {map}, exists? {map.get(nums[r])}.")
            
            if r - l > k:
                del map[nums[l]]
                l += 1
                continue

            if map.get(nums[r]) is not None:
                
                #print(f" i: {map.get(nums[r])}, j: {r}, returning True")
                
                return True
            
            map[nums[r]] = r    
            r += 1    

        return False