# sliding window, time:O(n), space: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = 0
        result = 0
        pre_zero_idx = -1
        while right < len(nums):
            if nums[right] == 0:
                left = pre_zero_idx + 1
                pre_zero_idx = right
            result = max(result, right-left+1)
            right += 1
        return result