#O(n^2), insertion sort
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        start = len(nums)-1
        for idx in range(1, len(nums)):      
            for idj in range(idx, 0, -1):
                if nums[idj-1] > nums[idj]:
                    self.swap(nums, idj, idj-1)
                    start = min(start, idj-1)
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
        