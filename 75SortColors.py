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
            
