class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        prefix = []
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        self.helper(prefix, nums, k, 0, result)
        return result
    def helper(self, prefix, nums, k, start, result):
        if k == 0:
            result.append(list(prefix))
        for idx, value in enumerate(nums[start:], start):
            prefix.append(value)
            self.helper(prefix, nums, k-1, idx+1, result)
            prefix.pop()
