class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for n in range(1, len(nums)):
            res = res ^ nums[n]
        return res
