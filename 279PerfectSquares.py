#memo
class Solution:
    def numSquares(self, n: int) -> int:
        self.table = {}
        return self.helper(n//2+1, n)
    def helper(self, start, target_sum):
        if target_sum == 0:
            return 0
        if target_sum < 0 or start < 1:
            return sys.maxsize
        if (start, target_sum) in self.table:
            return self.table[(start, target_sum)]
        result = sys.maxsize
        value = start**2
        count = 0
        while target_sum >= 0:
            result = min(result, count + self.helper(start-1, target_sum))
            count += 1
            target_sum -= value
        self.table[(start, target_sum)] = result
        return result
#DP
class Solution:
    def numSquares(self, n: int) -> int:
        value = 1
        table = [sys.maxsize for i in range(n+1)]
        table[0] = 0
        while value**2 <= n:
            for idx in range(value**2, len(table)):
                table[idx] = min(table[idx], table[idx-value**2]+1)
            value += 1
        return table[-1]