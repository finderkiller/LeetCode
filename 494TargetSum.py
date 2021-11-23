#brute force time: O(2^n), depth: O(n)
#memo
#time: O(n*t), space: O(n*t), depth: O(n)
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
    
#DP with hashmap lists
#time: O(n*t), space: (n*t)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        table = [{} for i in range(len(nums)+1)]
        table[0][0] = 1
        for idx in range(1, len(table)):
            nums_idx = idx-1
            for sum, count in table[idx-1].items():
                table[idx][sum+nums[nums_idx]] = table[idx].get(sum+nums[nums_idx], 0) + count
                table[idx][sum-nums[nums_idx]] = table[idx].get(sum-nums[nums_idx], 0) + count
        return table[-1].get(S, 0)
#DP with one hashmap
#time: O(n*t)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        cur_table = {}
        cur_table[0] = 1
        for num in nums:
            pre_table = cur_table
            cur_table = {}
            for key, value in pre_table.items():
                cur_table[key+num] = cur_table.get(key+num, 0)+value
                cur_table[key-num] = cur_table.get(key-num, 0)+value
        return cur_table[S] if S in cur_table else 0
                