#Back tracking
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        sum1 = 0
        sum2 = sum(nums)
        return self.helper(nums, 0, sum1, sum2)
    def helper(self, nums, start, sum1, sum2):
        if start == len(nums):
            return False
        for idx in range(start, len(nums)):
            sum1 += nums[idx]
            sum2 -= nums[idx]
            if sum1 == sum2:
                return True
            if self.helper(nums, idx+1, sum1, sum2):
                return True
            sum1 -= nums[idx]
            sum2 += nums[idx]
        return False
#DP
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 == 1:
            return False
        table = [False for i in range((total>>1) + 1)]
        table[0] = True
        
        for num in nums:
            for idx in range(len(table)-1, num-1, -1):
                table[idx] |= table[idx-num]
        return table[-1]