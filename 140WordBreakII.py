#brute force, backtracking
#time complexity: O(n*2^n+w) n is the length of string, w is the wordDict size
#Extra space: O(2^n*n+w), result裡面存了2^n種組合，每個組合的長度是n個字串，加上一開始見word_set, O(w)
#Depth: O(n)

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

#time complexity: O(n*2^n+w) n is the length of string, w is the wordDict size
#Extra space: O(2^n*n+w), result裡面存了2^n種組合，每個組合的長度是n個字串，加上一開始見word_set, O(w)
#Depth: O(n)
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
#time complexity: O(n^2 + 2^n + w), call edge還是O(2^n)次，但是有用memo紀錄過算過的，所以只會有n+n-1+...+1個edge，也就是n(n+1)/2，O(n^2)。雖然只有n^2個edge 但是每一個edge加總起來都還是會需要traverse 2^n 的組合結果，並且加上一開始要掃w建set)
#O(2^n*n+w)， result裡面存了2^n種組合，每個組合的長度是n個字串，加上一開始見word_set, O(w)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.word_set = set(wordDict)
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
            if string not in self.word_set:
                continue
            forward_list = self.helper(s, idx+1)
            for forward in forward_list:
                if forward == "":
                    result.append(string)
                else:
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
        word_set = set(wordDict)
        table = [[] for i in range(len(s)+1)]
        table[-1].append("")
        
        for idx in range(len(table)-2, -1, -1):
            string_start = idx
            result = []
            for string_end in range(string_start, len(s)):
                string = s[string_start:string_end+1]
                if string not in word_set:
                    continue
                for forward in table[string_end+1]:
                    if forward == "":
                        result.append(string)
                    else:
                        result.append(string + " " + forward)
            table[idx] = result
        return table[0]

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