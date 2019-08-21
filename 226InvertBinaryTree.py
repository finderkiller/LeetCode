# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.helper(root)
        return root
    def helper(self, node):
        if not node:
            return
        tmp = node.right
        node.right = node.left
        node.left = tmp
        self.helper(node.left)
        self.helper(node.right)
        
        