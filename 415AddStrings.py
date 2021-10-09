class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1:
            return nums2
        if not num2:
            return nums1
        idx1 = len(num1)-1
        idx2 = len(num2)-1
        carry = 0
        result = ""
        while idx1 >= 0 or idx2 >= 0:
            if idx1 < 0:
                num = (ord(num2[idx2]) - ord('0')) + carry
                carry = num//10
                result = str(num%10) + result
                idx2 -= 1
            elif idx2 < 0:
                num = (ord(num1[idx1]) - ord('0')) + carry
                carry = num//10
                result = str(num%10) + result
                idx1 -= 1
            else:
                num = (ord(num1[idx1]) - ord('0')) + (ord(num2[idx2]) - ord('0')) + carry
                carry = num//10
                result = str(num%10) + result
                idx1 -= 1
                idx2 -= 1
        if carry != 0:
            result = str(carry) + result
        return result