#hash table
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s:
            return []
        if len(s) < len(p):
            return []
        result = []
        table_p = self.buildFreqTable(p)
        table_substring = self.buildFreqTable(s[:len(p)])
        if self.isAnagrams(table_substring, table_p):
            result.append(0)
        left = 1
        right = len(p)
        while right < len(s):
            table_substring[s[left-1]] = table_substring.get(s[left-1], 0)-1
            table_substring[s[right]] = table_substring.get(s[right], 0)+1
            if self.isAnagrams(table_substring, table_p):
                result.append(left)
            left += 1
            right += 1
            
        return result
    def buildFreqTable(self, string):
        table = {}
        for char in string:
            table[char] = table.get(char, 0) +1
        return table
    def isAnagrams(self, table_substring, table_target):
        for key, value in table_target.items():
            if table_substring.get(key, 0) != value:
                return False
        return True