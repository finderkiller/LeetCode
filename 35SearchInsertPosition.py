class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        return self.helper(nums, 0, len(nums)-1, target)
        
    def helper(self, nums, start, end, target):
        if start >= end and nums[start] > target:
            return start
        if start >=end and nums[start] < target:
            return start + 1
        
        mid = (end-start)//2 + start
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.helper(nums, mid+1, end, target)
        else:
            return self.helper(nums, start, mid-1, target)
        
        