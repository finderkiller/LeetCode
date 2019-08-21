class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not equations or not values or not queries:
            return []
        if len(equations) != len(values):
            return []
        self.table = {}
        result = []
        for idx in range(len(equations)):
            equation = equations[idx]
            value = values[idx]
            if equation[0] not in self.table:
                self.table[equation[0]] = dict()
            if equation[1] not in self.table:
                self.table[equation[1]] = dict()
            self.table[equation[0]][equation[1]] = value
            self.table[equation[1]][equation[0]] = 1/value
        for query in queries:
            visited = set()
            result.append(self.helper(query[0], query[1], visited))
        return result
    
    def helper(self, start, end, visited):
        if start not in self.table:
            return -1
        if start == end:
            return 1
        if start in visited:
            return -1
        visited.add(start)
        for key, value in self.table[start].items():
            ret = self.helper(key, end, visited)
            if ret == -1:
                continue
            return value * ret
        return -1