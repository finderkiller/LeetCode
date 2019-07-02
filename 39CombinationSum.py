class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        prefix = []
        self.helper(candidates, prefix, target, result, 0)
        return result
        
    def helper(self, candidates, prefix, remain, result, start):
        if remain == 0:
            result.append(list(prefix))
            return
        if remain < 0:
            return
        for idx, value in enumerate(candidates[start:], start):
            prefix.append(value)
            self.helper(candidates, prefix, remain-value, result, idx)
            prefix.pop()
        return