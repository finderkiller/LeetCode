#O(n)
class Solution:
    def calculate(self, s: str) -> int:
        string = s.replace(' ', '')
        self.idx = 0
        return self.helper(string)
    def helper(self, s):
        operation = "+"
        current_number = 0
        result = 0
        while self.idx < len(s):
            if self.is_digit(s[self.idx]):
                current_number = 10*current_number + int(s[self.idx])
                self.idx += 1
            elif s[self.idx] == "+" or s[self.idx] == "-":
                result += current_number if operation == "+" else -current_number
                operation = s[self.idx]
                current_number = 0
                self.idx += 1
            elif s[self.idx] == "(":
                self.idx += 1
                forward = self.helper(s)
                result += forward if operation == "+" else -forward
            elif s[self.idx] == ")":
                result += current_number if operation == "+" else -current_number
                self.idx += 1
                return result
        result += current_number if operation == "+" else -current_number
        return result
                
    def is_digit(self, char):
        return ord('0') <= ord(char) <= ord('9')
            
                
                