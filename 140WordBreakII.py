#brute force, backtracking

class Solution(object):
    def wordBreak(self, s, wordDict):
        collect = []
        result = []
        self.table = set(wordDict)
        self.helper(collect, s, 0, result)
        return result
    
    def helper(self, collect, s, start, result):
        if start == len(s):
            result.append(" ".join(collect))
            return
        for idx in range(start, len(s)):
            string = s[start:idx+1]
            if string not in self.table:
                continue
            collect.append(string)
            self.helper(collect, s, idx+1, result)
            collect.pop()
        
#brute force, small to big
class Solution(object):
    def wordBreak(self, s, wordDict):
        self.dict = set(wordDict)
        return self.helper(s, 0)
    def helper(self, s, start):
        if start == len(s):
            return [""]
        result = []
        for idx in range(start, len(s)):
            string = s[start:idx+1]
            if string not in self.dict:
                continue
            forward_list = self.helper(s, idx+1)
            for forward in forward_list:
                if not forward:
                    result.append(string)
                    continue
                result.append(string + " " + forward)
        return result

#recursive, memo
class Solution(object):
    def wordBreak(self, s, wordDict):
        self.dict = set(wordDict)
        self.table = {}
        return self.helper(s, 0)
    def helper(self, s, start):
        if start == len(s):
            return [""]
        if start in self.table:
            return self.table[start]
        result = []
        for idx in range(start, len(s)):
            string = s[start:idx+1]
            if string not in self.dict:
                continue
            forward_list = self.helper(s, idx+1)
            for forward in forward_list:
                if not forward:
                    result.append(string)
                    continue
                result.append(string + " " + forward)
        self.table[start] = result
        return result
#DP, direction is the reversal of memo
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.wordDict = set(wordDict)
        self.table = [[] for i in range(len(s)+1)]
        self.table[-1].append("")
        for start in range(len(s)-1, -1, -1):
            for idx in range(start, len(s)):
                string = s[start:idx+1]
                if string not in self.wordDict:
                    continue
                for forward in self.table[idx+1]:
                    if len(forward) == 0:
                        self.table[start].append(string)
                    else:
                        self.table[start].append(string + " " + forward)
        return self.table[0]
#DP, direction is the same as memo
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.wordDict = set(wordDict)
        self.table = [[] for i in range(len(s)+1)]
        self.table[0].append("")
        for idx in range(1, len(self.table)):
            string_end = idx-1
            for string_start in range(string_end, -1, -1):
                string = s[string_start:string_end+1]
                if string not in self.wordDict:
                    continue
                for backward in self.table[string_start]:
                    if len(backward) == 0:
                        self.table[idx].append(string)
                    else:
                        self.table[idx].append(backward + " " + string)
        return self.table[-1]