class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.table = {}
        return self.helper(nums, target)
    def helper(self, nums, target):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target in self.table:
            return self.table[target]
        result = 0
        for num in nums:
            result += self.helper(nums, target - num)
        self.table[target] = result
        return result

#DP with the reversal direction of memo
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        table = [0 for i in range(target+1)]
        table[0] = 1
        for idx in range(1, target+1):
            for num in nums:
                if idx-num < 0:
                    continue
                table[idx] += table[idx-num]
        return table[-1] 

#DP, with the same direction of memo
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        table = [0 for i in range(target+1)]
        table[-1] = 1
        for idx in range(target, -1, -1):
            for num in nums:
                if idx+num >= len(table):
                    continue
                table[idx] += table[idx+num]
        return table[0]