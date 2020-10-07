class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, start, end):
        if start >= end:
            return nums[start]
        mid = start + (end-start)//2
        if mid-1>=0 and nums[mid-1] > nums[mid]:
            return nums[mid]
        if mid+1 < len(nums) and nums[mid+1] < nums[mid]:
            return nums[mid+1]
        if nums[mid] < nums[end]:
            return self.helper(nums, start, mid-1)
        else:
            return self.helper(nums, mid+1, end)