class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ""
        ret = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)-1, -1, -1):
            valuei = ord(num1[i]) - ord('0')
            carry = 0
            index = 0
            for j in range(len(num2)-1, -1, -1):
                valuej = ord(num2[j]) - ord('0')
                result = valuei * valuej
                index = i + j + 1
                result += carry
                result += ret[index]
                ret[index] = result % 10
                carry = result//10
            ret[index-1] = carry
        idx = 0
        while idx < len(ret):
            if ret[idx] != 0:
                break
            if idx == len(ret)-1:
                return str(0)
            idx += 1
        ret = ret[idx:]
        return "".join(map(str, ret))