    
"""
1.strip leading whitespace
2. find sign
3. traverse digit
    1. if find not digit, stop
4. consider range of number
    1. less than -2^31 return -2^31
    2. greater than 2^31-1 return 2^31-1
    





handle:
"word123" -> 0
"-123" -> -123
"+123" -> 123
"+word123" -> 0
"123word" ->123
"-00003" -> -3
"00003" -> 3


"""
#time: O(n), space: O(1)
class Solution:
    def myAtoi(self, string: str) -> int:
        if len(string) == 0:
            return 0
        string = string.strip()
        if len(string) == 0:
            return 0
        if not self.isdigit(string[0]) and not self.issign(string[0]):
            return 0
        idx = 0
        sign = 1
        cur = 0
        lower_bound = -(2**31)
        upper_bound = (2**31)-1
        if self.issign(string[0]):
            sign = 1 if string[0] == '+' else -1
            idx += 1
        while idx < len(string):
            if not self.isdigit(string[idx]):
                break
            cur = 10*cur + int(string[idx])
            idx += 1
        if sign*cur > upper_bound:
            return upper_bound
        if sign*cur < lower_bound:
            return lower_bound
        return sign*cur
        
    def isdigit(self, char):
        return ord(char) >= ord('0') and ord(char) <= ord('9')
    def issign(self, char):
        return char == '+' or char == '-'
        