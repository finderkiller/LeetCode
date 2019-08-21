"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#DFS, remember: traverse right first, and then traverse left
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        root.next = None
        self.helper(root)
        return root
    def helper(self, node):
        if not node:
            return
        nearest_right = self.findNearestRight(node)
        if node.right:
            node.right.next = nearest_right
        if node.left:
            node.left.next = node.right if node.right else nearest_right
        self.helper(node.right)
        self.helper(node.left)
    def findNearestRight(self, node):
        p = node.next
        while p != None:
            if p.left:
                return p.left
            if p.right:
                return p.right
            p = p.next
        return p

#BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        current = [root]
        while len(current) != 0:
            parent = current
            current = []
            for idx, node in enumerate(parent):
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
                if idx < len(parent)-1:
                    node.next = parent[idx+1]
        return root