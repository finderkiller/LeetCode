class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = []
        for idx in range(len(nums)):
            value = nums[idx]
            next_idx = abs(value)-1
            nums[next_idx] = 0-abs(nums[next_idx])
        
        for idx in range(len(nums)):
            if nums[idx] > 0:
                result.append(idx+1)
        return result
        