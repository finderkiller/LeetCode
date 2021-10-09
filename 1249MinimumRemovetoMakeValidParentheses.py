class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char == "(":
                stack.append(idx)
            elif char == ")" and len(stack) <= 0:
                s = s[:idx] + s[idx+1:]
                continue
            elif char == ")":
                stack.pop()
            idx += 1
        while len(stack) > 0:
            idx = stack.pop()
            s = s[:idx] + s[idx+1:]
        return s