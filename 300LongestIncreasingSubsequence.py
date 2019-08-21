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
        if not nums:
            return 0
        stack = [nums[0]]
        
        for idx in range(1, len(nums)):
            if nums[idx] > stack[-1]:
                stack.append(nums[idx])
                continue
            insert_index = self.findInsertIndex(stack, 0, len(stack)-1, nums[idx])
            stack[insert_index] = nums[idx]
        return len(stack)
    def findInsertIndex(self, stack, start, end, target):
        if start > end:
            return start
        mid = start + (end-start)//2
        if stack[mid] == target:
            return mid
        if stack[mid] < target:
            return self.findInsertIndex(stack, mid+1, end, target)
        else:
            return self.findInsertIndex(stack, start, mid-1, target)