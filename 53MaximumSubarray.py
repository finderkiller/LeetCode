class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_sum = 0 
        max_sum = -sys.maxsize-1
        for data in nums:
            if cur_sum + data < data:
                cur_sum = data
            else:
                cur_sum += data
            max_sum = max(max_sum, cur_sum)
        return max_sum