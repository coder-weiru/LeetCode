class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        map = {}
        results = []
        for n in range(len(nums)):
            map[nums[n]] = n
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in map and map[diff] != n:
                results.append([nums[n], diff])           
        
        return results
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr_map = {}
        for n in range(len(nums)):
            arr_map[nums[n]] = nums[0:n] + nums[n + 1:len(nums)]
        
        results = set()
        for k, v in arr_map.items():
            arr_list = self.twoSum(v, 0 - k)
            for a in arr_list:
                if a:
                    sorted_arr = a + [k]
                    sorted_arr.sort()
                    results.add(tuple(sorted_arr))

        return results
            