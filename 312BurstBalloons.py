#recursive, memo
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        self.table = {}
        return self.helper(nums, 1, len(nums)-2)
    def helper(self, nums, left, right):
        result = 0
        if (left, right) in self.table:
            return self.table[(left, right)]
        for idx in range(left, right+1):
            result = max(result, nums[left-1]*nums[idx]*nums[right+1] + self.helper(nums, left, idx-1) + self.helper(nums, idx+1, right))
        self.table[(left, right)] = result
        return result

#DP
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.insert(0, 1)
        nums.append(1)
        table = [[0 for i in range(len(nums))] for i in range(len(nums))]
        
        for right in range(1, len(table)-1):
            for left in range(right, 0, -1):
                for k in range(left, right+1):
                    table[right][left] = max(table[right][left], nums[left-1]*nums[k]*nums[right+1] + table[right][k+1] + table[k-1][left])
        return table[len(nums)-2][1]