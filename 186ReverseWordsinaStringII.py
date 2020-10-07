class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        for idx in range(len(s)):
            if s[idx] == " ":
                s[left:idx] = reversed(s[left:idx])
                left = idx + 1
        s[left:] = reversed(s[left:])
        s.reverse()
#using split
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        input = s.split()
        for idx in range(len(input)):
            input[idx] = input[idx][::-1]
        return " ".join(input)
        
        