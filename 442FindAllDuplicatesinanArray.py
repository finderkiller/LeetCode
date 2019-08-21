class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = []
        for idx in range(len(nums)):
            value = nums[idx]
            next_index = abs(value)-1
            if nums[next_index] < 0:
                result.append(abs(value))
            else:
                nums[next_index] = 0-nums[next_index]
        return result