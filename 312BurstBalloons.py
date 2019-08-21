#brute force
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        for idx in range(len(nums)):
            num = nums[idx]
            left = nums[idx-1] if idx-1 >= 0 else 1
            right = nums[idx+1] if idx+1 < len(nums) else 1
            current = left * nums[idx] * right 
            result = max(result, current + self.maxCoins(nums[:idx]+nums[idx+1:]))
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