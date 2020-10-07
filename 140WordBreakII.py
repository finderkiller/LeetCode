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
#DP
class Solution(object):
    def wordBreak(self, s, wordDict):
        dict = set(wordDict)
        table = [[] for i in range(len(s)+1)]
        table[0] = [""]
        
        for idx in range(1, len(table)):
            string_end = idx-1
            for string_start in range(string_end, -1, -1):
                string = s[string_start:string_end+1]
                if string not in dict:
                    continue
                for prev_string in table[idx-len(string)]:
                    if not prev_string:
                        table[idx].append(string)
                        continue
                    table[idx].append(prev_string + " " + string)
        return table[-1]