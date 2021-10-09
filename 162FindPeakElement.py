class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, start, end):
        if start >= end:
            return start
        mid = start + (end-start)//2
        if mid+1 <= end and nums[mid] < nums[mid+1]:
            return self.helper(nums, mid+1, end)
        return self.helper(nums, start, mid)