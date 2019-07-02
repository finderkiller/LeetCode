# is palindrome from each first index
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        prefix = []
        result = []
        self.helper(prefix, s, result)
        return result
    def helper(self, prefix, s, result):
        if len(s) == 0:
            result.append(list(prefix))
            return
        for idx in range(len(s)):
            if not self.isPalindrome(s, 0, idx):
                continue
            prefix.append(s[:idx+1])
            self.helper(prefix, s[idx+1:], result)
            prefix.pop()
            
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start +=1
            end -=1
        return True
# build palindrome dp table further, and then calculate all partitions
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        prefix = []
        result = []
        table = [[False for i in range(len(s))] for j in range(len(s))]
        for right in range(len(s)):
            table[right][right] = True
            for left in range(right):
                if left+1 == right:
                    table[right][left] = s[left] == s[right]
                if left+1 < right:
                    table[right][left] = s[left] == s[right] and table[right-1][left+1]
        self.helper(prefix, s, 0, table, result)
        return result
    def helper(self, prefix, s, start, table, result):
        if start == len(s):
            result.append(list(prefix))
            return
        for idx in range(start, len(s)):
            if not table[idx][start]:
                continue
            prefix.append(s[start:idx+1])
            self.helper(prefix, s, idx+1, table, result)
            prefix.pop()
