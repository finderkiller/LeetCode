class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = 1
        if x<0:
            sign = -1
        result = 0
        x = abs(x)
        while x != 0:
            result = result * 10 + x % 10
            x = x//10
        result *= sign
        return result if result <= 2**31-1 and result >= -(2**31) else 0