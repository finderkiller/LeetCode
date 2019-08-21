class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and needle:
            return -1
        if not needle:
            return 0
        for idx, char in enumerate(haystack):
            if char == needle[0] and idx+len(needle) <= len(haystack):
                string = haystack[idx:idx+len(needle)]
                if string == needle:
                    return idx
        return -1
                
                
                    