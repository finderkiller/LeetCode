#sol1: subproblems
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        return self.helper(len(nums)-1, nums)
    
    def helper(self, idx, nums):
        if idx == -1:
            return [[]]
        prev_list = self.helper(idx-1, nums)
        result = []
        for prev in prev_list:
            for insert_idx in range(len(prev)+1):
                result.append(prev[:insert_idx] + [nums[idx]] + prev[insert_idx:])
        return result

#sol2: backtracking
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

