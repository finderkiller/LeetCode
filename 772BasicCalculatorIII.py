class Solution:
    def calculate(self, s: str) -> int:
        self.idx = 0
        return self.helper(s)
        
    def helper(self, s):
        cur_num = 0
        stack = []
        pre_op = "+"
        while self.idx < len(s):
            letter = s[self.idx]
            if self.isdigit(letter):
                cur_num = 10*cur_num + int(letter)
                self.idx += 1
            if letter == "+" or letter == "-" or letter == "*" or letter == "/" or letter == ")":
                if pre_op == "+":
                    stack.append(cur_num)
                elif pre_op == "-":
                    stack.append(-cur_num)
                elif pre_op == "*":
                    stack.append(stack.pop()*cur_num)
                elif pre_op == "/":
                    top = stack.pop()
                    sign = 1 if top > 0 else -1
                    stack.append(abs(top)//cur_num * sign)
                self.idx += 1
                if letter == ")":
                    return sum(stack)
                else:
                    pre_op = letter
                    cur_num = 0
            elif letter == "(":
                self.idx += 1
                forward = self.helper(s)
                cur_num = forward
        if pre_op == "+":
            stack.append(cur_num)
        elif pre_op == "-":
            stack.append(-cur_num)
        elif pre_op == "*":
            stack.append(stack.pop()*cur_num)
        elif pre_op == "/":
            top = stack.pop()
            sign = 1 if top*cur_num > 0 else -1
            stack.append(abs(top)//abs(cur_num) * sign)
        return sum(stack)
                
    def isdigit(self, letter):
        return ord(letter) >= ord('0') and ord(letter) <= ord('9')