# bottom up
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        current = [1]
        return self.helper(current, 0, rowIndex)
    def helper(self, prev, index, rowIndex):
        if index == rowIndex:
            return prev
        current = [1]
        for idx, value in enumerate(prev):
            if idx == len(prev)-1:
                break
            current.append(value+prev[idx+1])
        current.append(1)
        return self.helper(current, index+1, rowIndex)

# top down
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        prev = self.getRow(rowIndex-1)
        current = [1]
        for idx, value in enumerate(prev):
            if idx == len(prev)-1:
                break
            current.append(value + prev[idx+1])
        current.append(1)
        return current