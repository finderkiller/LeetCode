#DP, scan twice
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        result = 0
        table=[0 for i in range(len(height))]
        leftmax = 0
        for idx in range(1, len(table)):
            leftmax = max(height[idx-1], leftmax)
            table[idx] = leftmax
        rightmax = 0
        for idx in range(len(table)-2, 0,-1):
            rightmax = max(rightmax, height[idx+1])
            lowerbound = min(table[idx], rightmax)
            if lowerbound > height[idx]:
                result += lowerbound-height[idx]
        return result
# left right pointer
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        leftmax = 0
        rightmax = 0
        result = 0
        
        while left <= right:
            if height[left] < height[right]:
                leftmax = max(leftmax, height[left])
                result += leftmax - height[left]
                left +=1
            else:
                rightmax = max(rightmax, height[right])
                result += rightmax - height[right]
                right -= 1
        return result
# decreasing mono stack
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        mono_stack = []
        result = 0
        idx = 0
        while idx < len(height):
            if len(mono_stack) == 0 or height[mono_stack[-1]] > height[idx]:
                mono_stack.append(idx)
                idx += 1
                continue
            top = mono_stack.pop()
            if len(mono_stack) == 0:
                continue
            left_idx = mono_stack[-1]
            result += (min(height[left_idx], height[idx])-height[top]) * (idx-left_idx-1)
        return result
        
        
        