class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0 or len(height) == 1:
            return 0
        
        max_area = 0
        start = 0
        end = len(height) - 1
        while start != end:
            area = (end - start) * min(height[start], height[end])
            max_area = max(area, max_area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area
        