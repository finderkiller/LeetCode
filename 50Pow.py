class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = abs(n)
        if n == 0:
            return 1
        return self.helper(x, n)
        
    def helper(self, x, n):
        if n == 0:
            return 1
        side1 = self.helper(x, n//2)
        side2 = side1
        if n % 2 ==1:
            side2 *= x
        return side1 * side2
        
#! bottom-up, but it would exceed limitation of memery if n is too big
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = abs(n)
        if n == 0:
            return 1
        return self.helper(x, n)
        
    def helper(self, x, n):
        result = [0] * (n+1)
        result[0] = 1
        result[1] = x
        
        for idx in range(2, len(result)):
            side1 = result[idx//2]
            side2 = side1
            if idx % 2 == 1:
                side2 *= x
            result[idx] = side1 * side2
        return result[n]
        