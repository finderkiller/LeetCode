#time: O(n)
#using method https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/1175295/Simplest-Python-Solution-with-O(N)-Easy-to-understand
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        digits = list('{0:b}'.format(n))
        sign = 1
        result = 0
        for idx, digit in enumerate(digits):
            if digit == '0':
                continue
            result += sign * (2**(len(digits)-idx)-1)
            sign *= -1
        return result