# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.helper(root, result, 0)
        return result
        
    def helper(self, node, result, level):
        if node == None:
            return
        if len(result) == level:
            result.append([node.val])
        elif level % 2 ==0:
            result[level].append(node.val)
        elif level % 2 == 1:
            result[level].insert(0, node.val)
        self.helper(node.left, result, level+1)
        self.helper(node.right, result, level+1)
        