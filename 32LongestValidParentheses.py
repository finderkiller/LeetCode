# sol1: brute force
# sol2: stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        max_length = 0
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            elif char == ")":
                if len(stack) != 0:
                    stack.pop()
                    if len(stack) != 0:
                        length = index - stack[-1]
                        max_length = max(max_length, length)
                    else:
                        stack.append(index)
                else:
                    return 0
        return max_length
