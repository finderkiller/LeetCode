#stack
#time: O(n)
#space: O(n)
"""
prev_operation = "+"
+3+2*2
stack[3,4], then 3+4
+3/2
stack[1]   3//2

+3+5/2
stack[3,2] 5//2

+3-5/2
stack[3,-2] abs(-5)//2 = -2

1. replace " " to ""
2. 


is_digit(), accumulate the operand

"""
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        s = s.replace(" ", "")
        stack = []
        cur_num = 0
        idx = 0
        pre_op = "+"
        while idx < len(s):
            letter = s[idx]
            if self.is_digit(letter):
                cur_num = 10*cur_num + int(letter)
            if not self.is_digit(letter) or idx == len(s)-1:
                if pre_op == "+":
                    stack.append(cur_num)
                elif pre_op == "-":
                    stack.append(-cur_num)
                elif pre_op == "*":
                    stack.append(stack.pop()*cur_num)
                elif pre_op == "/":
                    last_item = stack.pop()
                    sign = 1 if last_item > 0 else -1
                    stack.append(abs(last_item) // cur_num * sign)
                cur_num = 0
                pre_op = letter
            idx += 1
        return sum(stack)

    def is_digit(self, char):
        return ord('0') <= ord(char) and ord('9') >= ord(char)