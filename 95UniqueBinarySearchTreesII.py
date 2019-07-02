# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.helper(1, n)
    def helper(self, start, end):
        if start > end:
            return [None]
        result = []
        for value in range(start, end+1):
            left_sub_tree_list = self.helper(start,value-1)
            right_sub_tree_list = self.helper(value+1, end)
            for left_sub_tree in left_sub_tree_list:
                for right_sub_tree in right_sub_tree_list:
                    root = TreeNode(value)
                    root.left = left_sub_tree
                    root.right = right_sub_tree
                    result.append(root)
        return result
                    
                    
            
        