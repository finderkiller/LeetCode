class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        if not nums:
            return []
        result = [0]
        sorted_list = [nums[-1]]
        
        for idx in range(len(nums)-2, -1, -1):
            insert_point = bisect.bisect_left(sorted_list, nums[idx])
            result.insert(0, insert_point)
            sorted_list.insert(insert_point, nums[idx])
        return result