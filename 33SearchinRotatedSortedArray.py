class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.helper(nums, target, 0, len(nums)-1)
    def helper(self, nums, target, start, end):
        if start > end:
            return -1
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[end]:
            if target > nums[mid] and target <= nums[end]:
                return self.helper(nums, target, mid+1, end)
            else:
                return self.helper(nums, target, start, mid-1)
        else:
            if target >= nums[start] and target < nums[mid]:
                return self.helper(nums, target, start, mid-1)
            else:
                return self.helper(nums, target, mid+1, end)