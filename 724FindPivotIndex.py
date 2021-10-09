class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        total = sum(nums)
        pre_sum = 0
        for idx in range(len(nums)):
            if (total-nums[idx])%2 == 0 and pre_sum == (total-nums[idx])//2:
                return idx
            pre_sum += nums[idx]
        return -1