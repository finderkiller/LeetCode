# sorted, and find max:
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        nums = sorted(nums)
        return max(nums[0] * nums[1] * nums[-1], nums[-3]*nums[-2]*nums[-1])

# scan, find 2 number of min and 3 number of max
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
        