class Solution(object):
    def InsertionSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        for idx in range(1, len(nums)):
            idj = idx
            while idj > 0 and nums[idj-1] > nums[idj]:
                self.swap(nums, idj, idj-1)
                idj -= 1
        return nums
            
    def swap(self, nums, pos1, pos2):
        tmp = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = tmp


    def InsertionSort(self, nums):
        for idx in range(1, len(nums)):
            for idj in range(idx, 0, -1):
                if nums[idj-1] > nums[idj]:
                    self.swap(nums, idj-1, idj)
                else:
                    break
            
        