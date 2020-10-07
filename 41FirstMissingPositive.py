class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        length = len(nums)
        for idx in range(len(nums)):
            while nums[idx] > 0 and nums[idx] <= length and nums[nums[idx]-1] != nums[idx]:
                self.swap(nums, idx, nums[idx]-1)
        for idx, num in enumerate(nums):
            if num-1 != idx:
                return idx+1
        return length+1
                
    def swap(self, nums, pos1, pos2):
        if pos1 == pos2:
            return
        tmp = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = tmp
        