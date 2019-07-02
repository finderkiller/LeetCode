class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ""
        ret = [0] * (len(num1) + len(num2))
        carry = 0
        for i in range(len(num1)-1, -1, -1):
            valuei = ord(num1[i]) - ord('0')
            carry = 0
            index = 0
            for j in range(len(num2)-1, -1, -1):
                valuej = ord(num2[j]) - ord('0')
                index = i + j + 1
                result = valuei * valuej
                result += carry
                result += ret[index]
                ret[index] = result % 10
                carry = result // 10
            if carry != 0:
                ret[index-1] += carry
        idx = 0
        while idx < len(ret):
            if ret[idx] == 0 and len(ret) == 1:
                break
            if ret[idx] == 0:
                ret.pop(0)
                continue
            if ret[idx] != 0:
                break
        return "".join(map(str, ret))