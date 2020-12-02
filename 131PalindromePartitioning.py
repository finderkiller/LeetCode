# is palindrome from each first index
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        collect = []
        result = []
        self.helper(collect, s, 0, result)
        return result
        
    def helper(self, collect, string, start, result):
        if start == len(string):
            result.append(list(collect))
            return
        for idx in range(start, len(string)):
            tmp = string[start:idx+1]
            if not self.isPalindrome(tmp):
                continue
            collect.append(tmp)
            self.helper(collect, string, idx+1, result)
            collect.pop()

    def isPalindrome(self, string):
        if not string:
            return True
        left = 0
        right = len(string)-1
        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -=1
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
