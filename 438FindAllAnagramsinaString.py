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
        for idx in range(1, len(s)-len(p)+1):
            table_substring[s[idx-1]] = table_substring.get(s[idx-1], 0)-1
            table_substring[s[idx+len(p)-1]] = table_substring.get(s[idx+len(p)-1], 0)+1
            if self.isAnagrams(table_substring, table_p):
                result.append(idx)
        return result
        
    def buildFreqTable(self, string):
        table = {}
        for char in string:
            table[char] = table.get(char, 0) + 1
        return table
    def isAnagrams(self, table_s, table_p):
        for key,value in table_s.items():
            if value != table_p.get(key, 0):
                return False
        return True
        
            
        