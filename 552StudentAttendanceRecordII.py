# memo
# time: O(n*2*3), totalA == 0,1, continuousL == 0,1,2
# space: O(n*2*3), depth: O(n)
class Solution:
    def checkRecord(self, n: int) -> int:
        self.table = {}
        self.mod = 10**9+7
        return self.helper(n, 0, 0)
        
    def helper(self, n, totalA, continuousL):
        if n == 0:
            return 1
        result = 0
        if (n, totalA, continuousL) in self.table:
            return self.table[(n, totalA, continuousL)]
        if totalA == 0:
            result += self.helper(n-1, totalA+1, 0)
            result %= self.mod
        if continuousL < 2:
            result += self.helper(n-1, totalA, continuousL+1)
            result %= self.mod
        result += self.helper(n-1, totalA, 0)
        result %= self.mod
        self.table[(n, totalA, continuousL)] = result
        return result

#DP
# time: O(n*2*3), totalA == 0,1, continuousL == 0,1,2
# space: O(n*2*3)
class Solution:
    def checkRecord(self, n: int) -> int:
        self.mod = 10**9+7
        table = [[[0 for i in range(3)] for i in range(2)] for i in range(n+1)]
        for totalA in range(2):
            for continuousL in range(3):
                table[0][totalA][continuousL] = 1
                
        
        for idx in range(1, n+1):
            for totalA in [1, 0]:
                for continuousL in [2, 1, 0]:
                    if totalA == 0:
                        table[idx][totalA][continuousL] += table[idx-1][totalA+1][0]
                    if continuousL < 2:
                        table[idx][totalA][continuousL] += table[idx-1][totalA][continuousL+1]
                    table[idx][totalA][continuousL] += table[idx-1][totalA][0]
                    table[idx][totalA][continuousL] %= self.mod
        return table[-1][0][0]