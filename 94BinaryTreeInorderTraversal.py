# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result
    def helper(self, node, result):
        if node == None:
            return
        self.helper(node.left, result)
        result.append(node.val)
        self.helper(node.right, result)
        
        