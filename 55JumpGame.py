# top-down
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        table = set()
        return self.helper(nums, table, 0)
    def helper(self, nums, table, start):
        if start == len(nums)-1:
            return True
        if start in table:
            return True
        for step in range(1, nums[start]+1):
            if self.helper(nums, table, start+step):
                table.add(start)
                return True
        return False
        

# bottom-up
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        table = [False]*len(nums)
        table[len(nums)-1] = True
        for i in range(len(nums)-2, -1, -1):
            max_index = min(i+nums[i], len(nums)-1)
            for j in range(i+1, max_index+1):
                if table[j]== True:
                    table[i] = True
                    break
        return table[0]

# greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        leftmostgoodindex = len(nums)-1
        for index in range(len(nums)-2, -1, -1):
            if index + nums[index] >= leftmostgoodindex:
                leftmostgoodindex = index
        return leftmostgoodindex == 0
