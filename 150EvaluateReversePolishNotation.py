class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for value in tokens:
            if value != "+" and value != "-" and value != "*" and value != "/":
                stack.append(int(value))
                continue
            if len(stack) >= 2:
                result = 0
                b = stack.pop()
                a = stack.pop()
                if value == "+":
                    result = a + b
                if value == "-":
                    result = a - b
                if value == "*":
                    result = a * b
                if value == "/":
                    operator = 1 if a * b >= 0 else -1
                    result = abs(a) // abs(b) * operator
                stack.append(result)
            else:
                return 0
        return stack.pop()
        