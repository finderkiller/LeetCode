class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights.append(0)
        mono_stack = []
        max_area = 0
        idx = 0
        while idx < len(heights):
            if len(mono_stack) == 0 or heights[mono_stack[-1]] <= heights[idx]:
                mono_stack.append(idx)
                idx += 1
                continue
            cur_index = mono_stack.pop()
            if len(mono_stack) == 0:
                max_area = max(max_area, heights[cur_index]* (idx - (-1) -1))
                continue
            left_index = mono_stack[-1]
            max_area = max(max_area, heights[cur_index]* (idx-left_index-1))
        return max_area
            
            