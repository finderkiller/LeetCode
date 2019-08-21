#DP great:
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
#DP1:
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        table = [0 for i in range(len(nums))]
        for idx in range(len(table)):
            if idx-2 < 0:
                table[idx] = nums[idx]
            elif idx-2 == 0:
                table[idx] = nums[idx] + table[idx-2]
            else:
                table[idx] = nums[idx] + max(table[idx-2], table[idx-3])
        return max(table[-1], table[-2])
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
        