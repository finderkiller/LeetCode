#subproblem from first element
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.helper(nums, 0, result)
        return result
    def helper(self, nums, level, result):
        if level == len(nums):
            return
        prev_result = list(result)
        for element_list in prev_result:
            result.append(element_list + [nums[level]])
        self.helper(nums, level+1, result)
# subproblem from end element
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, 0)
        
    def helper(self, nums, level):
        if len(nums) == level:
            return [[]]
        next_result = self.helper(nums, level+1)
        result = []
        for element_list in next_result:
            new_set = list(element_list)
            new_set.insert(0, nums[level])
            result.append(new_set)
        return result + next_result

# back tracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        prefix = []
        result = []
        result.append(prefix)
        self.helper(prefix, nums, 0, result)
        return result
        
    def helper(self, prefix, nums, start, result):
        if start == len(nums):
            return 
        for idx in range(start, len(nums)):
            prefix.append(nums[idx])
            result.append(list(prefix))
            self.helper(prefix, nums, idx+1, result)
            prefix.pop()
        return
