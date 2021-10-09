# brute force, back tracking
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        collect = []
        self.helper(collect, result, 2, n)
        return result
        
    def helper(self, collect, result, start, n):
        if n == 1:
            if len(collect) > 1:
                result.append(list(collect))
            return
        for factor in range(start, n+1):
            if n%factor != 0:
                continue
            collect.append(factor)
            self.helper(collect, result, factor, n//factor)
            collect.pop()