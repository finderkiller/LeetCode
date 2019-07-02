class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b,a)
        result = ""
        diff = len(a)-len(b)
        for i in range(diff):
            b = '0'+b
        carry = 0
        for idx in range(len(a)-1, -1, -1):
            valuea = int(a[idx])
            valueb = int(b[idx])
            sum = valuea+valueb+carry
            result = str(sum%2)+result
            carry = sum//2
        if carry != 0:
            result = str(carry) + result
        return result
