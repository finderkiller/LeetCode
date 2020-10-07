class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        tmp = ""
        result = ""
        for char in s:
            if char == " ":
                if tmp != "":
                    stack.append(tmp)
                    tmp = ""
                continue
            tmp += char
        if tmp!= "":
            stack.append(tmp)
        return " ".join(reversed(stack))
#simple method
class Solution(object):
    def reverseWords(self, s):
        if not s:
            return ""
        input = s.split()
        left = 0 
        right = len(input)-1
        while left <right:
            tmp = input[left]
            input[left] =input[right]
            input[right] = tmp
            left += 1
            right -= 1
        return " ".join(input)
        
        
            
        