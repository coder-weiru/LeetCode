class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for n in range(len(nums)):
            map[nums[n]] = n
        for n in range(len(nums)):
            diff = target - nums[n]
            if diff in map and map[diff] != n:
                return [n, map[diff]]                