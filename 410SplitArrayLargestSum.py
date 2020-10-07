#brute force
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        return self.helper(nums, 0, -sys.maxsize, m)
    def helper(self, nums, start, current_max, m):
        if m == 1:
            return max(current_max, sum(nums[start:]))
        result = sys.maxsize
        for idx in range(start, len(nums)-m+1):
            current_max = max(sum(nums[start:idx+1]), current_max)
            result = min(result, self.helper(nums, idx+1, current_max, m-1))
        return result
#DP
class Solution(object):
    def splitArray(self, nums, m):
        if not nums:
            return 0
        table = [[sys.maxsize for i in range(len(nums)+1)] for j in range(m+1)]
        table[0][0] = 0
        prev_sum = [0]
        for num in nums:
            prev_sum.append(prev_sum[-1]+num)
        
        for divide in range(1, len(table)):
            for prev_nums in range(divide, len(table[0])):
                for k in range(divide-1, prev_nums):
                    back_sum = prev_sum[prev_nums]-prev_sum[k]
                    table[divide][prev_nums] = min(table[divide][prev_nums], max(table[divide-1][k], back_sum))
                
        return table[-1][-1]