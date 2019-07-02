class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            if char == "]":
                if stack and stack[len(stack)-1] == "[":
                    stack.pop()
                else:
                    return False
        
            if char == ")":
                if stack and stack[len(stack)-1] == "(":
                    stack.pop()
                else:
                    return False
                
            if char == "}":
                if stack and stack[len(stack)-1] == "{":
                    stack.pop()
                else:
                    return False
        return True if not stack else False