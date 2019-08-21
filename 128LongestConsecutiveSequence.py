class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = set(nums)
        max_length = 0
        for num in nums:
            length = 1
            pre = num-1
            next = num+1
            while pre in table:
                length += 1
                table.remove(pre)
                pre-=1
            while next in table:
                length += 1
                table.remove(next)
                next+=1
            max_length = max(max_length, length)
        return max_length
        
        