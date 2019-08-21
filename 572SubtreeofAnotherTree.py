# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        if s.val == t.val and self.helper(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def helper(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.helper(s.left, t.left) and self.helper(s.right, t.right)
        