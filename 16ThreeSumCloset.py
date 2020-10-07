class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return target
        nums = sorted(nums)
        result = 0
        diff = sys.maxsize
        for first_idx in range(len(nums)-2):
            start = first_idx+1
            end = len(nums)-1
            while start < end:
                threesum = nums[first_idx] + nums[start] + nums[end]
                if threesum > target:
                    end -= 1
                elif threesum < target:
                    start += 1
                else:
                    return threesum
                if abs(threesum-target) < diff:
                    diff = abs(threesum-target)
                    result = threesum
        return result