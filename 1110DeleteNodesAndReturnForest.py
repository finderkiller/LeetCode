# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        delete_set = set(to_delete)
        result = []
        root = self.helper(root, delete_set, result)
        if root:
            result.append(root)
        return result
        
    def helper(self, node, delete_set, result):
        if not node:
            return
        node.left = self.helper(node.left, delete_set, result)
        node.right = self.helper(node.right, delete_set, result)
        if node.val in delete_set:
            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)
            return None
        return node
                
        