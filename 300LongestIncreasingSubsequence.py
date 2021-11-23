#DP O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        table = [1 for i in range(len(nums))]
        
        max_length = 0
        for idx in range(len(table)):
            value = nums[idx]
            for nums_idx in range(0, idx):
                if nums[nums_idx] < value:
                    table[idx] = max(table[idx], table[nums_idx] + 1)
            max_length = max(max_length, table[idx])
        return max_length

#DP  O(nlogm), n is the lengh of nums, m is the length of LIS
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        import bisect
        for num in nums:
            insert_point = bisect.bisect_left(stack, num)
            if insert_point < len(stack):
                stack.pop(insert_point)
            stack.insert(insert_point, num)
        return len(stack)