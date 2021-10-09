class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findStart(nums, 0, len(nums)-1, target), self.findLast(nums, 0, len(nums)-1, target)]
        
    def findStart(self, nums, start, end, target):
        if start > end:
            return -1
        mid = start + (end-start)//2
        if nums[mid] == target:
            if mid-1 >=0 and nums[mid-1] == target:
                return self.findStart(nums, start, mid-1, target)
            else:
                return mid
        elif nums[mid] > target:
            return self.findStart(nums, start, mid-1, target)
        else:
            return self.findStart(nums, mid+1, end, target)
    def findLast(self, nums, start, end, target):
        if start > end:
            return -1
        mid = start + (end-start)//2
        if nums[mid] == target:
            if mid+1 < len(nums) and nums[mid+1] == target:
                return self.findLast(nums, mid+1, end, target)
            else:
                return mid
        elif nums[mid] > target:
            return self.findLast(nums, start, mid-1, target)
        else:
            return self.findLast(nums, mid+1, end, target)