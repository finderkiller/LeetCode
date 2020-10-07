class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not S:
            return ""
        string = "".join(S.split("-"))
        start = len(string)%K
        ans = string[:start].upper()
        remain = string[start:].upper()
        idx = 0
        while idx < len(remain):
            if ans != "" and idx%K == 0:
                ans += "-"
            ans += remain[idx]
            idx += 1
        return ans
            