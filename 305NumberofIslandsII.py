


class UnionFind:
    def __init__(self, N):
        self.parent = []
        self.rank = []
        self.count = 0
        for i in range(N):
            self.parent.append(-1)
            self.rank.append(0)
    
    def setParent(self, idx):
        if self.parent[idx] >= 0:
            return
        self.parent[idx] = idx
        self.count += 1
    
    def find(self, val):
        if self.parent[val] != val:
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
    
    def isValid(self, idx):
        return self.parent[idx] >= 0
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m*n)
        result = []
        for row, col in positions:
            cur_index = col+row*n
            uf.setParent(cur_index)
            overlap = []
            if row - 1 >= 0 and uf.isValid((row-1)*n+col):
                overlap.append((row-1)*n+col)
            if row + 1 < m and uf.isValid((row+1)*n+col):
                overlap.append((row+1)*n+col)
            if col - 1 >= 0 and uf.isValid(row*n+col-1):
                overlap.append(row*n+col-1)
            if col + 1 < n and uf.isValid(row*n+col+1):
                overlap.append(row*n+col+1)
            for idx in overlap:
                uf.union(idx, cur_index)
            result.append(uf.count)
        return result