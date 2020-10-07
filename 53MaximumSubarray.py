class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = nums[0]
        result = nums[0]
        for idx in range(1, len(nums)):
            if max_sum + nums[idx] < nums[idx]:
                max_sum = nums[idx]
            else:
                max_sum += nums[idx]
            result =max(result, max_sum)
        return result