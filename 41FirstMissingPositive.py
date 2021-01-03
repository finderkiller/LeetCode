class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums):
            if nums[idx] > 0 and nums[idx] < len(nums) and nums[idx] != nums[nums[idx]-1]:
                self.swap(nums, idx, nums[idx]-1)
            else:
                idx += 1
        for idx in range(len(nums)):
            value = idx+1
            if nums[idx] != value:
                return value
        return len(nums)+1
            
            
    def swap(self, nums, a, b):
        tmp  = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp
        