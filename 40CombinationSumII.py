class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        prefix = []
        if not candidates:
            return result
        self.helper(sorted(candidates), target, prefix, result, 0)
        return result
    def helper(self, candidates, remain, prefix, result, start):
        if remain < 0:
            return
        if remain == 0:
            result.append(list(prefix))
            return
        for idx, value in enumerate(candidates[start:], start):
            if idx != start and candidates[idx] == candidates[idx-1]:
                continue
            prefix.append(value)
            self.helper(candidates, remain-value, prefix, result, idx+1)
            prefix.pop()
        return
        