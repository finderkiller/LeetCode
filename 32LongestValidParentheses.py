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
#DP
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        table = [0 for i in range(len(s))]
        max_length = 0
        for idx, char in enumerate(s):
            if char == '(':
                continue
            elif idx-1 >= 0 and s[idx-1] == '(':
                table[idx] = table[idx-2]+2 if idx-2 >=0 else 2
            elif idx-table[idx-1]-1 >= 0 and s[idx-table[idx-1]-1] == '(':
                table[idx] = table[idx-table[idx-1]-2]+table[idx-1]+2 if idx-table[idx-1]-2 >=0 else table[idx-1]+2
            max_length = max(max_length, table[idx])
        return max_length