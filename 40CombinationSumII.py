# time: O(2^n), space: for collect, O(N)
# depth: O(N)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return []
        collect = []
        result = []
        nums = sorted(candidates)
        self.helper(collect, nums, 0, 0, target, result)
        return result
    
    def helper(self, collect, nums, start, current, target, result):
        if current == target:
            result.append(list(collect))
            return
        if current > target:
            return
        for idx in range(start, len(nums)):
            if idx != start and nums[idx] == nums[idx-1]:
                continue
            collect.append(nums[idx])
            self.helper(collect, nums, idx+1, current+nums[idx], target, result)
            collect.pop()