# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isMirror(root.left, root.right)
    def isMirror(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False
        if node1.val == node2.val:
            return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)
        return False
        