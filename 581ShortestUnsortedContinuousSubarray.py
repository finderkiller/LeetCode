#O(n^2), insertion sort
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        start = len(nums)-1
        for idx in range(1, len(nums)):
            if nums[idx] >= nums[idx-1]:
                continue
            j = idx
            while j > 0 and nums[j] < nums[j-1]:
                self.swap(nums, j ,j-1)
                j -= 1
            start = min(start, j)
            result = max(result, idx-start+1)
        return result
    def swap(self, nums, pos1, pos2):
        tmp = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = tmp
#using sorted nums
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        left = 0
        right = len(sorted_nums)-1
        while left < len(nums):
            if nums[left] != sorted_nums[left]:
                break
            left += 1
        while right > left:
            if nums[right] != sorted_nums[right]:
                break
            right -= 1
        return right-left+1
        