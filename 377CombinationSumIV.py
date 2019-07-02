#! memorization
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        table = {}
        return self.helper(nums, table, target)
    
    def helper(self, nums, table, target):
        if target < 0:
            return 0
        if target == 0:
            return 1
        if target in table:
            return table[target]
        count = 0
        for value in nums:
            remain = target - value
            count += self.helper(nums, table, remain)
        table[target] = count
        return table[target]

#! DP
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        result = [0] * (target + 1)
        result[0] = 1
        for i in range(1, len(result)):
            for num in nums:
                if i-num >= 0:
                    result[i] += result[i-num]
        return result[target]