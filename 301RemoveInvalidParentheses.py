

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        ub_left = 0
        ub_right = 0
        result = []
        for char in s:
            if char == "(":
                ub_left += 1
            elif char == ")" and ub_left == 0:
                ub_right += 1
            elif char == ")":
                ub_left -= 1
        self.helper(0, ub_left, ub_right, s, result)
        return result
    def helper(self, start, left, right, s, result):
        if left == 0 and right == 0 and self.isValid(s):
            result.append(s)
            return
        for idx in range(start, len(s)):
            if idx != start and s[idx] == s[idx-1]:
                continue
            if s[idx] == "(" and left > 0:
                self.helper(idx, left-1, right, s[:idx]+s[idx+1:], result)
            elif s[idx] == ")" and right > 0:
                self.helper(idx, left, right-1, s[:idx]+s[idx+1:], result)
                
    def isValid(self, s):
        left = 0
        for char in s:
            if char == "(":
                left += 1
            elif char == ")":
                left -= 1
            if left < 0:
                return False
        return True