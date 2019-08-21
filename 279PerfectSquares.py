#memo
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        self.table = {}
        return self.helper(n)
    def helper(self, n):
        if n < 0:
            return sys.maxsize
        if n == 0:
            return 0
        if n in self.table:
            return self.table[n]
        idx = 1
        ways = sys.maxsize
        while (n-idx**2)>=0:
            ways = min(ways, self.helper(n-idx**2))
            idx += 1
        self.table[n] = ways+1
        return ways+1
#DP
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        table = [sys.maxsize for i in range(n+1)]
        table[0] = 0
        
        for idx in range(1, n+1):
            j = 1
            while idx - j**2 >=0:
                table[idx] = min(table[idx-j**2]+1, table[idx])
                j+=1
        return table[n]