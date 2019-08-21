#memo
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        self.table = {}
        return self.helper(nums, 0, 0, S)
    def helper(self, nums, start, current_sum, target):
        if len(nums) == start and current_sum == target:
            return 1
        if len(nums) == start:
            return 0
        if (current_sum, start) in self.table:
            return self.table[(current_sum, start)]
        self.table[(current_sum, start)] = self.helper(nums, start+1, current_sum+nums[start], target) + self.helper(nums, start+1, current_sum-nums[start], target)
        return self.table[(current_sum, start)]
    
#DP with hashmap lists:
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        table = [dict() for i in range(len(nums)+1)]
        table[0][0] = 1
        
        for i in range(1, len(table)):
            nums_index = i-1
            for sum, count in table[i-1].items():
                prev_value = table[i].get(sum+nums[nums_index], 0)
                table[i][sum+nums[nums_index]] = count + prev_value
                
                prev_value = table[i].get(sum-nums[nums_index], 0)
                table[i][sum-nums[nums_index]] = count + prev_value
        return table[-1].get(S, 0)
#DP with one hashmap
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        table = {}
        table[0] = 1
        for i in range(0, len(nums)):
            next_table = {}
            nums_index = i
            for sum, count in table.items():
                prev_value = next_table.get(sum+nums[nums_index], 0)
                next_table[sum+nums[nums_index]] = count + prev_value
                
                prev_value = next_table.get(sum-nums[nums_index], 0)
                next_table[sum-nums[nums_index]] = count + prev_value
                table = next_table
        return table.get(S, 0)
                