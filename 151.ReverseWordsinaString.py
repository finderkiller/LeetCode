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
            
        
            
        