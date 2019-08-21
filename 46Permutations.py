class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        collect = []
        result = []
        self.helper(collect, nums, result)
        return result
    def helper(self, collect, nums, result):
        if len(nums) == 0:
            result.append(list(collect))
            return
        for idx, value in enumerate(nums):
            collect.append(value)
            self.helper(collect, nums[:idx] + nums[idx+1:], result)
            collect.pop()