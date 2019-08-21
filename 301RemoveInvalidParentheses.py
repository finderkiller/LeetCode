class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        result = []
        left = 0
        right = 0
        for char in s:
            if char == "(":
                left += 1
            elif left == 0 and char == ")":
                right += 1
            elif char == ")":
                left -= 1
        self.helper(s, 0, left, right, result)
        return result
    def helper(self, string, start, left, right, result):
        if left == 0 and right == 0 and self.isValid(string):
            result.append(string)
            return
        for idx, char in enumerate(string[start:], start):
            if idx>start and char == string[idx-1]:
                continue
            if left!=0 and char == "(":
                self.helper(string[:idx]+string[idx+1:], idx, left-1, right, result)
            if right!=0 and char == ")":
                self.helper(string[:idx]+string[idx+1:], idx, left, right-1, result)
    def isValid(self, string):
        if not string:
            return True
        right = 0
        left = 0
        for char in string:
            if char == ")":
                right +=1
            elif char == "(":
                left +=1
            if right > left:
                return False
        if left > right:
            return False
        return True