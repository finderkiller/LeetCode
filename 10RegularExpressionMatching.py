class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == None or p == None:
            return False
        #!dp = [[False] * (len(p) + 1)] * (len(s) + 1)
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(dp[0])):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-2]
       
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j] |= dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[len(s)][len(p)]