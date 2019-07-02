"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#DFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.helper(root)
        return root
    def helper(self, root):
        if root == None:
            return
        if root.left != None:
            root.left.next = root.right
        if root.right != None:
            root.right.next = root.next.left if root.next != None else None
        self.helper(root.left)
        self.helper(root.right)
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
            return root
        current = [root]
        while len(current) > 0:
            parent = current
            current = []
            for idx, node in enumerate(parent):
                if node.left != None:
                    current.append(node.left)
                if node.right != None:
                    current.append(node.right)
                if idx == len(parent) - 1:
                    break
                node.next = parent[idx+1]
        return root

#using two pointer
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        start = root
        while start != None:
            cur = start
            while cur != None:
                if cur.left:
                    cur.left.next = cur.right
                if start.right:
                    cur.right.next = cur.next.left if cur.next else None
                cur = cur.next
            start = start.left
        return root