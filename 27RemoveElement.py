class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1