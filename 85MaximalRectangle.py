class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        heights = [0 for i in range(len(matrix[0]))]
        max_rec = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    heights[col] = 0
                else:
                    heights[col] += 1
            max_rec = max(max_rec, self.helper(heights))
        return max_rec
    def helper(self, heights):
        if not heights:
            return 0
        heights.append(0)
        stack = []
        idx = 0
        max_rec = 0
        while idx < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[idx]:
                stack.append(idx)
                idx += 1
                continue
            top = stack.pop()
            if len(stack) == 0:
                max_rec = max(max_rec, heights[top]*idx)
                continue
            max_rec = max(max_rec, heights[top]* (idx-stack[-1]-1))
        return max_rec
        
                    