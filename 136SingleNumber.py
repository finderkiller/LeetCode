class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return
        result = nums[0]
        for value in nums[1:]:
            result ^= value
        return result
        