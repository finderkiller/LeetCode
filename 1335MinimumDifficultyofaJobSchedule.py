#memo
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        self.table = {}
        return self.helper(jobDifficulty, 0, d)
        
    def helper(self, array, start, days):
        if days == 1:
            return max(array[start:])
        if (start, days) in self.table:
            return self.table[(start, days)]
        result = sys.maxsize
        for idx in range(start, len(array)-days+1):
            difficulty = max(array[start:idx+1])
            forward = self.helper(array, idx+1, days-1)
            result = min(result, difficulty + forward)
        self.table[(start, days)] = result
        return result

#DP
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        table = [[sys.maxsize for i in range(len(jobDifficulty))] for i in range(d)]
        for day in range(len(table)):
            for index in range(len(table[0])-1, -1, -1):
                if day == 0:
                    table[day][index] = max(jobDifficulty[index:])
                    continue
                for idx in range(index, len(jobDifficulty)-day):
                    difficulty = max(jobDifficulty[index:idx+1])
                    table[day][index] = min(table[day][index], difficulty+table[day-1][idx+1])
        return table[-1][0]