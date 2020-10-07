class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        table = {}
        result = []
        for idx, equation in enumerate(equations):
            if equation[0] not in table:
                table[equation[0]] = {}
            table[equation[0]][equation[1]] = values[idx]
            if equation[1] not in table:
                table[equation[1]] = {}
            table[equation[1]][equation[0]] = 1/values[idx]
        for query in queries:
            self.visited = set()
            result.append(self.helper(table, query[0], query[1]))
        return result
            
    def helper(self, table, start, end):
        if start not in table:
            return -1
        if start == end:
            return 1
        self.visited.add(start)
        for key, value in table[start].items():
            if key in self.visited:
                continue
            ret = self.helper(table, key, end)
            if ret == -1:
                continue
            return ret * value
        self.visited.remove(start)
        return -1