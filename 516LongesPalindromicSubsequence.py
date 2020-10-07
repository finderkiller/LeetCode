#recursive, time:O(2^n), space:O(n)
#recursive, memo, time:(n^2), space: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.table = {}
        return self.helper(s, 0, len(s)-1)
    def helper(self, s, left, right):
        if left > right:
            return 0
        if left == right:
            return 1
        if (left, right) in self.table:
            return self.table[(left, right)]
        if s[left] == s[right]:
            self.table[(left, right)] = self.helper(s, left+1, right-1) + 2
        else:
            self.table[(left, right)] = max(self.helper(s, left+1, right), self.helper(s, left, right-1))
        return self.table[(left, right)]
#DP, time: O(n^2), space: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        table = [[0 for i in range(len(s))] for i in range(len(s))]
        
        for right in range(len(table)):
            for left in range(right, -1, -1):
                if right == left:
                    table[right][left] = 1
                elif s[right] == s[left]:
                    table[right][left] = table[right-1][left+1] + 2
                else:
                    table[right][left] = max(table[right-1][left], table[right][left+1])
        return table[len(s)-1][0]