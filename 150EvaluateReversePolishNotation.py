#stack
#time: O(n), space: O(n)
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if not self.is_operator(token):
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(b+a)
                elif token == "-":
                    stack.append(b-a)
                elif token == "*":
                    stack.append(b*a)
                elif token == "/":
                    sign = 1 if b*a > 0 else -1
                    stack.append(abs(b)//abs(a) * sign)
        return stack[-1]
        
    def is_operator(self, letter):
        return letter == "+" or letter == "-" or letter == "/" or letter == "*"
        