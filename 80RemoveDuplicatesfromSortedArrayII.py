class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        j = 1
        has_duplicated = False
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                has_duplicated = False
            elif nums[i] == nums[j] and not has_duplicated:
                i += 1
                nums[i] = nums[j]
                has_duplicated = True
            j += 1
        return i+1