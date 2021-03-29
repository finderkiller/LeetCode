class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0
        length = len(bin(max(nums)))-1
        for idx in range(length, -1, -1):
            result <<= 1
            prefix = set()
            cur_max = result | 1
            for num in nums:
                prefix.add(num>>idx)
            for pre in prefix:
                if pre ^ cur_max in prefix:
                    result |= 1
        return result
        