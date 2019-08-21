class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        for j in range(len(nums)):
            if nums[j] != 0:
                i+=1
                self.swap(nums, i, j)
    def swap(self, nums, pos1, pos2):
        tmp = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = tmp
        