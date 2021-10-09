class Solution:
    def checkValidString(self, s: str) -> bool:
        left_count = 0
        right_count = 0
        for char in s:
            if char == ")":
                left_count -= 1
            else:
                left_count += 1
            if left_count < 0:
                return False
        if left_count == 0:
            return True
        for idx in range(len(s)-1, -1, -1):
            char = s[idx]
            if char == "(":
                right_count -= 1
            else:
                right_count += 1
            if right_count < 0:
                return False
        return True