class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        collect = []
        result =[]
        self.helper(collect, 1, n, k, result)
        return result
    def helper(self, collect, start, n, k, result):
        if k == 0:
            result.append(list(collect))
            return
        for num in range(start, n+1):
            collect.append(num)
            self.helper(collect, num+1, n, k-1, result)
            collect.pop()