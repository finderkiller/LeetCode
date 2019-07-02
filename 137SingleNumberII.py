class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums))//2
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for idx in range(32):
            mask = 1 << idx
            sum = 0
            for value in nums:
                if value & mask:
                    sum += 1
            result = result | (sum%3 << idx)
        return self.convert(result)
    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x
            
        