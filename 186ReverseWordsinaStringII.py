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