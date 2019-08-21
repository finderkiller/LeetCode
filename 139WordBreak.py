# top down
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        word_set = set(wordDict)
        return self.helper(s, 0, word_set)
    def helper(self, s, start, word_set):
        if start == len(s):
            return True
        for idx in range(start, len(s)):
            string = s[start:idx+1]
            if string in word_set and self.helper(s, idx+1, word_set):
                return True
        return False

# memo
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        word_set = set(wordDict)
        table = {}
        return self.helper(s, 0, table, word_set)
    def helper(self, s, start, table, word_set):
        if start == len(s):
            return True
        if start in table:
            return table[start]
        for idx in range(start, len(s)):
            string = s[start:idx+1]
            if string in word_set and self.helper(s, idx+1, table, word_set):
                table[start] = True
                return True
        table[start] = False
        return False
#DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        word_dict = set(wordDict)
        table = [False for i in range(len(s)+1)]
        table[0] = True
        for idx in range(1, len(table)):
            string_end = idx-1
            for string_start in range(string_end, -1, -1):
                string = s[string_start:string_end+1]
                if string in word_dict and table[idx-len(string)]:
                    table[idx] = True
                    break
        return table[-1]
            
        