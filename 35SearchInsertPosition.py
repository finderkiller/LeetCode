class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        return self.helper(nums, 0, len(nums)-1, target)
    def helper(self, nums, start, end, target):
        if start > end:
            return start
        mid = start+(end-start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.helper(nums, mid+1, end, target)
        else:
            return self.helper(nums, start, mid-1, target)