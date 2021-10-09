class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        result = 0
        left = 0
        right = 0
        while right < len(s):
            char = s[right]
            if char in table:
                left = max(left, table.get(char)+1)
            table[char] = right
            result = max(result, right-left+1)
            right += 1
        return result