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
        self.flatten(root.left)
        self.flatten(root.right)
        left_tail = root.left
        right_head = root.right
        if not left_tail:
            return
        while left_tail.right:
            left_tail = left_tail.right
        root.right = root.left
        root.left = None
        left_tail.right = right_head