class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_count = 0
        invalid_right_count = 0
        for char in s:
            if char == "(":
                left_count += 1
            elif char == ")" and left_count == 0:
                invalid_right_count += 1
            elif char == ")":
                left_count -= 1
        return invalid_right_count+left_count