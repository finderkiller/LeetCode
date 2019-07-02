class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = self.helper(n)
        return [int(string, 2) for string in result]
    def helper(self, n):
        if n == 0:
            return ['0']
        if n == 1:
            return ['0', '1']
        prev_list = self.helper(n-1)
        result = []
        for prev in prev_list:
            result.append('0' + prev)
        for prev in reversed(prev_list):
            result.append('1' + prev)
        return result
            
        
