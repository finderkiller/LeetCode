class Solution(object):
    def BubbleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted = True
        for idx in range(len(nums)-1, 0, -1):
            for idj in range(0, idx):
                if nums[idj] > nums[idj+1]:
                    sorted = False
                    self.swap(nums, idj, idj+1)
            if sorted:
                return nums
        return nums
            
    def swap(self, nums, pos1, pos2):
        tmp = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = tmp