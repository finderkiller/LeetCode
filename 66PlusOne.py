class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        carry = 0
        for idx in range(len(digits)-1, -1, -1):
            value = digits[idx]
            if idx == len(digits)-1:
                sum = value+carry+1
            else:
                sum = value + carry
            digits[idx] = sum % 10
            carry = sum//10
        if carry != 0:
            digits.insert(0, carry)
        return digits
