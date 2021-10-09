class Solution:
    def isHappy(self, n: int) -> bool:
        table = set()
        while n != 1:
            if n in table:
                return False
            table.add(n)
            result = 0
            for char in str(n):
                result += int(char)**2
            n = result
        return True