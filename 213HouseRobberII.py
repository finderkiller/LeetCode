#recursive, memo
class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        self.table = {}
        return max(nums[0] + self.helper(nums, 2, True), self.helper(nums, 1, False))
        
    def helper(self, nums, idx, rob_first):
        if idx == len(nums)-1 and rob_first:
            return 0
        if idx >= len(nums):
            return 0
        if (idx, rob_first) in self.table:
            return self.table[(idx, rob_first)]
        self.table[(idx, rob_first)] = max(nums[idx] + self.helper(nums, idx+2, rob_first), self.helper(nums, idx+1, rob_first))
        return self.table[(idx, rob_first)]
# recursive, memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        self.table = {}
        not_rob_first = self.helper(nums[1:], 0)
        self.table = {}
        not_rob_last = self.helper(nums[:len(nums)-1], 0)
        return max(not_rob_first, not_rob_last)
    def helper(self, nums, idx):
        if idx >= len(nums):
            return 0
        if idx in self.table:
            return self.table[idx]
        self.table[idx] = max(nums[idx]+self.helper(nums, idx+2), self.helper(nums, idx+1))
        return self.table[idx]
#DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        not_rob_first = self.helper(nums[1:])
        not_rob_last = self.helper(nums[:len(nums)-1])
        return max(not_rob_first, not_rob_last)
    def helper(self, nums):
        table = [0 for i in range(len(nums))]
        table[0] = nums[0]
        table[1] = max(nums[1], nums[0])
        for idx in range(2, len(nums)):
            table[idx] = max(nums[idx]+table[idx-2], table[idx-1])
        return table[-1]
#DP, only using two variable
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        not_rob_first = self.helper(nums[1:])
        not_rob_last = self.helper(nums[:len(nums)-1])
        return max(not_rob_first, not_rob_last)
    def helper(self, nums):
        last_two = 0
        last_one = 0
        for num in nums:
            cur = max(num+last_two, last_one)
            last_two = last_one
            last_one = cur
        return last_one