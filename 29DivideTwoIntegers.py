class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = True
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            sign = False
        
        result = self.helper(abs(dividend), abs(divisor))
        return result if sign else 0-result
        
        
    def helper(self, dividend, divisor):
        if dividend < divisor:
            return 0
        return 1 + self.divide(dividend - divisor, divisor)
        