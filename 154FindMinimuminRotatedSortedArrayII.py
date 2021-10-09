class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)
    
    def helper(self, nums, start, end):
        if start >= end:
            return nums[start]
        mid = start + (end-start)//2
        if mid-1 >= 0 and nums[mid-1] > nums[mid]:
            return nums[mid]
        elif mid+1 < len(nums) and nums[mid+1] < nums[mid]:
            return nums[mid+1]
        if nums[mid] < nums[end]:
            return self.helper(nums, start, mid-1)
        elif nums[mid] > nums[end]:
            return self.helper(nums, mid+1, end)
        else:
            if nums[mid] != nums[start]:
                return self.helper(nums, start, mid-1)
        return min(self.helper(nums, start, mid-1), self.helper(nums, mid+1, end))