class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        max_contain = nums[:3]
        max_contain = sorted(max_contain)
        
        min_contain = nums[:2]
        min_contain = sorted(min_contain)
        
        
        for value in nums[3:]:
            if max_contain[0] < value:
                max_contain[0] = value
                max_contain = sorted(max_contain)
        for value in nums[2:]:
            if min_contain[1] > value:
                min_contain[1] = value
                min_contain = sorted(min_contain)
        
        return max(max_contain[0] * max_contain[1] * max_contain[2], min_contain[0] * min_contain[1] * max_contain[2])
        