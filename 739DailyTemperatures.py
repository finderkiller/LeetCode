class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        result = [0 for i in range(len(T))]
        stack = []
        idx= 0 
        while idx < len(T):
            if len(stack) == 0 or T[stack[-1]] >= T[idx]:
                stack.append(idx)
                idx += 1
                continue
            cur_idx = stack.pop()
            result[cur_idx] = idx-cur_idx
        return result
        