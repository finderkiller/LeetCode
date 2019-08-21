class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k:
            return []
        collect = []
        result = []
        self.helper(collect, 1, k, n, result)
        return result
    def helper(self, collect, start, k, target, result):
        if len(collect) == k and target == 0:
            result.append(list(collect))
            return
        if len(collect) > k or target < 0:
            return
        for num in range(start, 10):
            collect.append(num)
            self.helper(collect, num+1, k, target-num, result)
            collect.pop()