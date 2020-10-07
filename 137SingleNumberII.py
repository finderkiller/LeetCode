class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums))//2
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:  
        result = 0
        for idx in range(32):
            mask = 1 << idx
            total = 0
            for num in nums:
                if num & mask:
                    total += 1
            result = result + ((total % 3) << idx)
        if result >= 2**31:
            return -(2**31) + (result & ((1<<31) - 1))
        return result
            
        