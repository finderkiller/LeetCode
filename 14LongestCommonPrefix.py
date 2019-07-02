class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        table = {}
        prefix = strs[0]
        for s in strs[1:]:
            while (s.find(prefix) !=0):
                prefix = prefix[:len(prefix)-1]
            if prefix == "":
                return ""
        return prefix