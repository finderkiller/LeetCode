# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        if root.left:
            nextStart = root.right
            root.right = root.left
            root.left = None
            tmp = root.right
            while tmp.right != None:
                tmp = tmp.right
            tmp.right = nextStart
        