class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        start = 0
        for idx in range(len(s)):
            if s[idx] == " ":
                tmp = str(s[start:idx][::-1])
                output += tmp + " "
                start = idx+1
        tmp = str(s[start:][::-1])
        output += tmp
        return output
            
        