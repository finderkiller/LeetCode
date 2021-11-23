class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for i in range(size)]
        
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for a,b in edges:
            if not uf.union(a-1,b-1):
                return [a, b]