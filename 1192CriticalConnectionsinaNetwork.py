#DFS, time:O(E*E), space: O(v)
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        depend_table = defaultdict(set)
        result = []
        for node_a, node_b in connections:
            depend_table[node_a].add(node_b)
            depend_table[node_b].add(node_a)
        
        for node_a, node_b in connections:
            self.visited = set()
            depend_table[node_a].remove(node_b)
            depend_table[node_b].remove(node_a)
            if not self.helper(node_a, node_b, depend_table):
                result.append([node_a, node_b])
            depend_table[node_a].add(node_b)
            depend_table[node_b].add(node_a)
        return result
            
    def helper(self, node, target, depend_table):
        if node == target:
            return True
        self.visited.add(node)
        for child in depend_table.get(node):
            if child in self.visited:
                continue
            if self.helper(child, target, depend_table):
                return True
        return False

#Tarjan's Algorithm
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        depend_table = defaultdict(set)
        for node_a, node_b in connections:
            depend_table[node_a].add(node_b)
            depend_table[node_b].add(node_a)
    
        self.result = []
        self.step = [-1] * n
        self.helper(0, -1, 0, depend_table)
        return self.result
            
    def helper(self, cur, par, level, depend_table):
        self.step[cur] = level
        
        for child in depend_table.get(cur):
            if child == par:
                continue
            elif self.step[child] == -1:
                self.step[cur] = min(self.step[cur], self.helper(child, cur, level+1, depend_table))
            else:
                self.step[cur] = min(self.step[cur], self.step[child])
        if cur!= 0 and self.step[cur] == level:
            self.result.append([par, cur])
        return self.step[cur]
        