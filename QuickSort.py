class Solution(object):
    def QuickSort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        self.helper(nums, 0, len(nums)-1)
        return nums
    def helper(self, nums, start, end):
        if start >= end:
            return
        pivot_idx = random.randint(start, end)
        self.swap(nums, pivot_idx, end)
        pivot_value = nums[end]
        i = start-1
        j = start
        while j < end:
            if nums[j] <= pivot_value:
                i += 1
                self.swap(nums, i, j)
            j += 1
        i += 1
        self.swap(nums, i, end)
        self.helper(nums, start, i-1)
        self.helper(nums, i+1, end)
        
    def swap(self, nums, pos1, pos2):
        tmp = nums[pos1]
        nums[pos1] = nums[pos2]
        nums[pos2] = tmp