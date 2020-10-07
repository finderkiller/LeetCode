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

#since it has sorted, using start > cur_sum/cur_count
class Solution(object):
    def combinationSum3(self, k, n):
        if n==0:
            return []
        collect = []
        result = []
        self.helper(collect, 1, k, n, result)
        return result
        
    def helper(self, collect, start, cur_count, cur_sum, result):
        if cur_sum == 0 and cur_count == 0:
            result.append(list(collect))
            return
        if cur_sum == 0 or cur_count == 0:
            return
        if start > cur_sum/cur_count:
            return
        for num in range(start, 10):
            collect.append(num)
            self.helper(collect, num+1, cur_count-1, cur_sum-num, result)
            collect.pop()