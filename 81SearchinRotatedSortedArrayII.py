class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        return self.helper(nums, 0, len(nums)-1, target)
        
    def helper(self, nums, start, end, target):
        if start > end:
            return False
        mid = start + (end-start) // 2
        if nums[mid] == target:
            return True
        if nums[mid] < nums[end]:
            if target > nums[mid] and target <=nums[end]:
                return self.helper(nums, mid+1, end, target)
            else:
                return self.helper(nums, start, mid-1, target)
        elif nums[mid] > nums[end]:
            if target >= nums[start] and target < nums[mid]:
                return self.helper(nums, start, mid-1, target)
            else:
                return self.helper(nums, mid+1, end, target)
        else:
            if nums[mid] != nums[start]:
                return self.helper(nums, start, mid-1, target)
            result = self.helper(nums, start, mid-1, target)
            if not result:
                result = self.helper(nums, mid+1, end, target)
            return result