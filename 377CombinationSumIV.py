class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.table = {}
        return self.helper(nums, 0, target)
        
    def helper(self, nums, current, target):
        if current == target:
            return 1
        if current > target:
            return 0
        if current in self.table:
            return self.table[current]
        result = 0
        for num in nums:
            result += self.helper(nums, current+num, target)
        self.table[current] = result
        return result

#DP
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