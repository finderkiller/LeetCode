class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        s = s.replace(" ", "")
        stack = []
        pre_operator = "+"
        cur_num = 0
        result = 0
        for idx, char in enumerate(s):
            if self.is_digit(char):
                cur_num = cur_num*10 + int(char)
            if not self.is_digit(char) or idx == len(s)-1:
                if pre_operator == "+":
                    stack.append(cur_num)
                elif pre_operator == "-":
                    stack.append(-cur_num)
                elif pre_operator == "*":
                    stack.append(stack.pop()*cur_num)
                elif pre_operator == "/":
                    top = stack.pop()
                    if top < 0:
                        stack.append(-(abs(top)//cur_num))
                    else:
                        stack.append(top//cur_num)
                cur_num = 0
                pre_operator = char
        for num in stack:
            result += num
        return result
        
    def is_digit(self, char):
        return ord('0') <= ord(char) and ord('9') >= ord(char)