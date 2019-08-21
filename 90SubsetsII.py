class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums = sorted(nums)
        collect = []
        result = [[]]
        self.helper(collect, nums, 0, result)
        return result
    def helper(self, collect, nums, start, result):
        if start == len(nums):
            return
        for idx in range(start, len(nums)):
            if idx != start and nums[idx] == nums[idx-1]:
                continue
            collect.append(nums[idx])
            result.append(list(collect))
            self.helper(collect, nums, idx+1, result)
            collect.pop()