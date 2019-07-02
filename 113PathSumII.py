# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result= []
        prefix = []
        self.helper(prefix, root, sum, result)
        return result
    def helper(self, prefix, node, sum, result):
        if node == None:
            return
        prefix.append(node.val)
        if node.left == None and node.right == None and sum-node.val == 0:
            result.append(list(prefix))
            prefix.pop()
            return
        self.helper(prefix, node.left, sum-node.val, result)
        self.helper(prefix, node.right, sum-node.val, result)
        prefix.pop()