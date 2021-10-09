# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        deleted_set = set(to_delete)
        result = []
        self.helper(result, root, deleted_set)
        if root.val not in deleted_set:
            result.append(root)
        return result
        
    def helper(self, result, node, deleted_set):
        if not node:
            return
        node.left = self.helper(result, node.left, deleted_set)
        node.right = self.helper(result, node.right, deleted_set)
        if node.val in deleted_set:
            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)
            return None
        return node
                
        