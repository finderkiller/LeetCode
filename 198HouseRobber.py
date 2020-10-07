#DP:
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        table = [0 for i in range(len(nums))]
        table[0] = nums[0]
        table[1] = max(nums[0], nums[1])
        for idx in range(2, len(table)):
            table[idx] = max(nums[idx] + table[idx-2] , table[idx-1])
        return table[-1]
#DP, only using two variable
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        last_one = 0
        last_two = 0
        for num in nums:
            cur = max(num+last_two, last_one)
            last_two = last_one
            last_one = cur
        return last_one
#memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.table = {}
        return self.helper(nums, 0)
    def helper(self, nums, start):
        if start >= len(nums):
            return 0
        if start in self.table:
            return self.table[start]
        result = max(nums[start] + self.helper(nums, start+2), self.helper(nums, start+1))
        self.table[start] = result
        return result
        