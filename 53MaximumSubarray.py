class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize-1
        sum = 0
        for num in nums:
            if sum < 0:
                sum = num
            else:
                sum += num
            max_sum = max(max_sum, sum)
        return max_sum