# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return
        self.result = sys.maxsize
        self.helper(root, target)
        return self.result
        
    def helper(self, node, target):
        if not node:
            return
        if abs(target-node.val) < abs(target-self.result):
            self.result = node.val
        self.helper(node.left, target)
        self.helper(node.right, target)

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return
        self.result = sys.maxsize
        self.helper(root, target)
        return self.result
        
    def helper(self, node, target):
        if not node:
            return
        if abs(target-node.val) < abs(target-self.result):
            self.result = node.val
        if target < node.val:
            self.helper(node.left, target)
        elif target > node.val:
            self.helper(node.right, target)