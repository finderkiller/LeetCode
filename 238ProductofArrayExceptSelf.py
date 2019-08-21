class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = [1 for i in range(len(nums))]
        for idx in range(1, len(res)):
            res[idx] = nums[idx-1] * res[idx-1]
            
        right = 1
        for idx in range(len(res)-2, -1, -1):
            right *= nums[idx+1]
            res[idx] *= right
        return res
            
        
        