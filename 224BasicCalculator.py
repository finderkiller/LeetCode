#recursive: O(n)
"""
recursive see each (
return see each )
is_digit
pre_operator,
handle if see char not digit

2-1+(2-3+4)
2-(3+4+6)


"""

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        s=s.replace(" ", "")
        self.idx = 0
        return self.helper(s)
        
    def helper(self, s):
        cur_num = 0
        result = 0
        pre_operator = "+"
        while self.idx < len(s):
            letter = s[self.idx]
            if self.is_digit(letter):
                cur_num = cur_num*10 + int(letter)
                self.idx += 1
            elif letter == "+" or letter == "-":
                result += cur_num if pre_operator == "+" else -cur_num
                pre_operator = letter
                self.idx += 1
                cur_num = 0
            elif letter == "(":
                self.idx += 1
                forward = self.helper(s)
                cur_num = forward
            elif letter == ")":
                result += cur_num if pre_operator == "+" else -cur_num
                self.idx += 1
                return result
        result += cur_num if pre_operator == "+" else -cur_num
        return result
                
    def is_digit(self, letter):
        return ord(letter) >= ord('0') and ord(letter) <= ord('9')
            
                
                