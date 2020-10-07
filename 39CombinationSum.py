class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target <= 0:
            return []
        collect = []
        self.result = []
        self.helper(collect, 0, candidates, 0, target)
        return self.result
    
    def helper(self, collect, start, candidates, cur_sum, target):
        if cur_sum == target:
            self.result.append(list(collect))
            return
        if cur_sum > target:
            return
        for idx in range(start, len(candidates)):
            collect.append(candidates[idx])
            self.helper(collect, idx, candidates, cur_sum+candidates[idx], target)
            collect.pop()
        