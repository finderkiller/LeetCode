class Solution(object):
    def MergeSort(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, start, end):
        if start >= end:
            return [nums[start]]
        mid = start + (end-start)//2
        l1 = self.helper(nums, start, mid)
        l2 = self.helper(nums, mid+1, end)
        return self.merge(l1, l2)
    def merge(self, l1, l2):
        ret = []
        idx1 = 0
        idx2 = 0
        while idx1 < len(l1) or idx2 < len(l2):
            if idx1 == len(l1):
                ret.append(l2[idx2])
                idx2 += 1
            elif idx2 == len(l2):
                ret.append(l1[idx1])
                idx1 += 1
            elif l1[idx1] <= l2[idx2]:
                ret.append(l1[idx1])
                idx1 += 1
            else:
                ret.append(l2[idx2])
                idx2 += 1
        return ret