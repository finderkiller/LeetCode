class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = []
        current = [1]
        result.append(current)
        self.helper(numRows, result)
        return result
    def helper(self, numRows, result):
        if len(result) == numRows:
            return
        prev = result[-1]
        current = [1]
        for idx, value in enumerate(prev):
            if idx == len(prev)-1:
                break
            current.append(value + prev[idx+1])
        current.append(1)
        result.append(current)
        self.helper(numRows, result)