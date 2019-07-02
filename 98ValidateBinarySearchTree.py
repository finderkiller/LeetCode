# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -sys.maxsize-1, sys.maxsize)
    def helper(self, node, min_value, max_value):
        if node == None:
            return True
        if node.val <= min_value or node.val >= max_value:
            return False
        return self.helper(node.left, min_value, node.val) and self.helper(node.right, node.val, max_value)
        