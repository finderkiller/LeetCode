class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        remainder_count = len(nums)
        #table = self.getFrequency(nums)
        #self.permuteUniqueImpl([], table, remainder_count, result)
        
        self.helper([], sorted(nums), result)
        return result
    def helper(self, prefix, remain, result):
        if len(remain) == 0:
            result.append(list(prefix))
        for idx,value in enumerate(remain):
            if idx != 0 and remain[idx] == remain[idx-1]:
                continue
            prefix.append(value)
            self.helper(prefix, remain[:idx] + remain[idx+1:], result)
            prefix.pop()
        return
            
        
    def getFrequency(self, nums):
        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        return table
    
    def permuteUniqueImpl(self, prefix, table, remainder_count, result):
        if remainder_count == 0:
            result.append(prefix)
            return
        for key, value in table.items():
            if (value > 0):
                table[key] -= 1
                next = list(prefix)
                next.append(key)
                self.permuteUniqueImpl(next, table, remainder_count-1, result)
                table[key] += 1
                
        return 