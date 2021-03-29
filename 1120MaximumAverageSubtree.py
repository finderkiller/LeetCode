# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.maxAve = -sys.maxsize-1
        self.helper(root)
        return self.maxAve
        
    def helper(self, node):
        if not node:
            return (0, 0)
        left_sum, left_count = self.helper(node.left)
        right_sum, right_count = self.helper(node.right)
        total_sum = left_sum+right_sum+node.val
        total_count = left_count+right_count+1
        self.maxAve = max(self.maxAve, total_sum/total_count)
        return (total_sum, total_count)
        