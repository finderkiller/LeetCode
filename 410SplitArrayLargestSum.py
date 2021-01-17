#brute force
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        return self.helper(nums, 0, m)
    
    def helper(self, nums, start, m):
        if m == 1:
            return sum(nums[start:])
        result = sys.maxsize
        for idx in range(start, len(nums)-m+1):
            cur_sum = sum(nums[start:idx+1])
            forward = self.helper(nums, idx+1, m-1)
            result = min(result, max(cur_sum, forward))
        return result

#memo
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.table = {}
        return self.helper(nums, 0, m)
    
    def helper(self, nums, start, m):
        if m == 1:
            return sum(nums[start:])
        if (start, m) in self.table:
            return self.table[(start, m)]
        result = sys.maxsize
        for idx in range(start, len(nums)-m+1):
            cur_sum = sum(nums[start:idx+1])
            forward = self.helper(nums, idx+1, m-1)
            result = min(result, max(cur_sum, forward))
        self.table[(start, m)] = result
        return result
#DP direction is the reversal of memo
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.table = [[sys.maxsize for i in range(len(nums))] for i in range(m)]
        for start in range(len(nums)):
            self.table[0][start] = sum(nums[start:])
        for m in range(1, len(self.table)):
            for start in range(len(nums)-1, -1, -1):
                for idx in range(start, len(nums)-m):
                    cur_sum = sum(nums[start:idx+1])
                    forward = self.table[m-1][idx+1]
                    self.table[m][start] = min(self.table[m][start], max(cur_sum, forward))
        return self.table[-1][0]

#DP direction is the reversal of memo with back_sum
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.table = [[sys.maxsize for i in range(len(nums))] for i in range(m)]
        back_sum = []
        for start in range(len(nums)):
            self.table[0][start] = sum(nums[start:])
            back_sum.append(sum(nums[start:]))
        for m in range(1, len(self.table)):
            for start in range(len(nums)-1, -1, -1):
                for idx in range(start, len(nums)-m):
                    cur_sum = back_sum[start] - back_sum[idx+1]
                    forward = self.table[m-1][idx+1]
                    self.table[m][start] = min(self.table[m][start], max(cur_sum, forward))
        return self.table[-1][0]

#DP direction is the same with memo:
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.table = [[sys.maxsize for i in range(len(nums))] for i in range(m)]
        for end in range(len(nums)):
            self.table[0][end] = sum(nums[:end+1])
        for m in range(1, len(self.table)):
            for end in range(len(nums)):
                for idx in range(m, end+1):
                    cur_sum = sum(nums[idx:end+1])
                    backward = self.table[m-1][idx-1]
                    self.table[m][end] = min(self.table[m][end], max(cur_sum, backward))
        return self.table[-1][-1]
#DP direction is the same with memo and with prev_sum:
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self.table = [[sys.maxsize for i in range(len(nums))] for i in range(m)]
        prev_sum = []
        for end in range(len(nums)):
            self.table[0][end] = sum(nums[:end+1])
            prev_sum.append(sum(nums[:end+1]))
        for m in range(1, len(self.table)):
            for end in range(len(nums)):
                for idx in range(m, end+1):
                    cur_sum = prev_sum[end] - prev_sum[idx-1]
                    backward = self.table[m-1][idx-1]
                    self.table[m][end] = min(self.table[m][end], max(cur_sum, backward))
        return self.table[-1][-1]
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