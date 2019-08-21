# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.sum = 0
        self.helper(root)
        return root
    def helper(self, node):
        if not node:
            return
        self.helper(node.right)
        node.val += self.sum
        self.sum = node.val
        self.helper(node.left)