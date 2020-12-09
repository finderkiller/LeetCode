# O(n), xor
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = nums[0]
        for num in nums[1:]:
            result = result ^ num
        return result
# O(logn), bineary search
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, start, end):
        if start >= end:
            return nums[start]
        mid = start + (end-start)//2
        if mid-1 >=0 and nums[mid] == nums[mid-1]:
            if mid % 2 == 1:
                return self.helper(nums, mid+1, end)
            else:
                return self.helper(nums, start, mid-2)
        elif mid+1 < len(nums) and nums[mid] == nums[mid+1]:
            if mid % 2 == 0:
                return self.helper(nums, mid+2, end)
            else:
                return self.helper(nums, start, mid-1)
        else:
            return nums[mid]
            