class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        string = s.strip()
        idx = 0
        while idx < len(string):
            if string[idx] == ' ':
                string = string[idx+1:]
                idx = 0
            else:
                idx += 1
        return len(string)
