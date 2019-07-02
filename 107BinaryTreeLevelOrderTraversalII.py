# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.helper(root, result, 0)
        result.reverse()
        return result
    def helper(self, node, result, level):
        if node == None:
            return
        if len(result) == level:
            result.append([node.val])
        else:
            result[level].append(node.val)
        self.helper(node.left, result, level+1)
        self.helper(node.right, result, level+1)