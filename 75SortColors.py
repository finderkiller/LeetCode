# time: O(n), space: O(1), but not one pass
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        table = [0] * 3
        for value in nums:
                table[value] += 1
        nums_index = 0
        for idx, value in enumerate(table):
            for i in range(value):
                nums[nums_index] = idx
                nums_index += 1
            

# time: O(n), space: O(1), one pass, two pointer
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        idx = 0
        first_idx = 0
        last_idx = len(nums)-1
        while idx <= last_idx:
            value = nums[idx]
            if value == 0:
                self.swap(nums, idx, first_idx)
                first_idx += 1
                idx += 1
            elif value == 1:
                idx += 1
            elif value == 2:
                self.swap(nums, idx, last_idx)
                last_idx -= 1
        return nums
                
    def swap(self, nums, a, b):
        tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp
