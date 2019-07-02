# building from the subsets of n-1 nums
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        result = []
        prev_list = self.subsets(nums[1:])
        value = nums[0]
        for prev in prev_list:
            newset = list(prev)
            newset.insert(0, value)
            result.append(newset)
        result += prev_list
        return result

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
