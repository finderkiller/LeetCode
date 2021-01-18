class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        depend_table = defaultdict(set)
        for idx, connection in enumerate(isConnected):
            for idy in range(len(connection)):
                if idy == idx:
                    continue
                if connection[idy] == 1:
                    depend_table[idx].add(idy)
        self.visited = set()
        result = 0
        for node in range(len(isConnected[0])):
            if node in self.visited:
                continue
            result += 1
            self.helper(node, depend_table)
        return result
    def helper(self, node, depend_table):
        self.visited.add(node)
        for child in depend_table.get(node, []):
            if child in self.visited:
                continue
            self.helper(child, depend_table)