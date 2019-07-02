"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        result = Node(node.val, [])
        table = {}
        table[node.val] = result
        queue = [node]
        while len(queue) > 0:
            cur = queue.pop(0)
            for neighbor in cur.neighbors:
                if neighbor.val not in table:
                    new_node = Node(neighbor.val, [])
                    table[neighbor.val] = new_node
                    table[cur.val].neighbors.append(new_node)
                    queue.append(neighbor)
                else:
                    table[cur.val].neighbors.append(table[neighbor.val])
        return result
#DFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        table = {}
        return self.dfs(node, table)
    def dfs(self, node, table):
        if node.val in table:
            return table[node.val]
        new_node = Node(node.val, [])
        table[node.val] = new_node
        for neighbor in node.neighbors:
            copy_node = self.dfs(neighbor, table)
            new_node.neighbors.append(copy_node)
        return new_node
        