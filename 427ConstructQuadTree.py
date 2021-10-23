"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
import numpy as np
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        grid = np.array(grid)
        return self.helper(grid)
    
    def helper(self, grid):
        n = len(grid)
        if self.check_leaf(grid):
            return Node(bool(grid[0][0]), True, None, None, None, None)
        topleft = grid[:n//2, :n//2]
        topright = grid[:n//2, n//2:]
        bottomleft = grid[n//2:, :n//2]
        bottomright = grid[n//2:, n//2:]
        
        return Node(bool(grid[0][0]), False, \
                   self.helper(topleft), \
                   self.helper(topright), \
                   self.helper(bottomleft), \
                   self.helper(bottomright))
        
    def check_leaf(self, grid):
        val = grid[0][0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != val:
                    return False
        return True