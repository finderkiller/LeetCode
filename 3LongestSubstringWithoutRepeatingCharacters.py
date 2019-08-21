class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0 
        runner = 0
        max_length = 0
        table = {}
        while runner < len(s):
            char = s[runner]
            if char in table:
                start = max(start, table[char]+1)
            max_length = max(runner-start+1, max_length)
            table[char] = runner
            runner += 1
        return max_length