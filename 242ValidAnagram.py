class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        table  = {}
        for char in s:
            if char in table:
                table[char] += 1
            else:
                table[char] = 1
        
        for char in t:
            if char not in table:
                return False
            table[char] -= 1
            if table[char] < 0:
                return False
        return True

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        