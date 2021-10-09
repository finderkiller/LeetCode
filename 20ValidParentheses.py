class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif not stack:
                return False
            elif char == ')' and stack[-1] != '(':
                return False
            elif char == ']' and stack[-1] != '[':
                return False
            elif char == '}' and stack[-1] != '{':
                return False
            else:
                stack.pop()
        return len(stack) == 0