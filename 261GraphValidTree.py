#sol1: brute Force, find cycle or not when add each edge
#time: O(n*n), 
#sol2: union find
#time: O(n)
#space: O(n)

"""
1. union for edges, if found they have had the same root, return False
2. check they have the same root
"""
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        self.size = size
        
    def findParent(self, index):
        if self.parent[index] != index:
            self.parent[index] = self.findParent(self.parent[index])
        return self.parent[index]
    
    def union(self, a, b):
        roota = self.findParent(a)
        rootb = self.findParent(b)
        
        if roota == rootb:
            return False
        if self.rank[roota] > self.rank[rootb]:
            self.parent[rootb] = roota
        elif self.rank[roota] < self.rank[rootb]:
            self.parent[roota] = rootb
        else:
            self.parent[rootb] = roota
            self.rank[roota] += 1
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        
        for a, b in edges:
            if not uf.union(a, b):
                return False
        root_set = set()
        for index in range(n):
            root_set.add(uf.findParent(index))
        return len(root_set) == 1