# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        length_post = len(postorder)
        length_in = len(inorder)
        if length_post != length_in:
            return None
        self.table = {}
        for idx, value in enumerate(inorder):
            self.table[value] = idx
        return self.helper(inorder, postorder, 0, length_in-1, 0, length_post-1)
    def helper(self, inorder, postorder, start_in, end_in, start_post, end_post):
        if start_in > end_in or start_post > end_post:
            return None
        node = TreeNode(postorder[end_post])
        node_idx = -1
        if node.val in self.table:
            node_idx = self.table[node.val]
        else:
            return None
        left_tree_size = node_idx - start_in
        right_tree_size = end_in - node_idx
        node.left = self.helper(inorder, postorder, start_in, node_idx-1, start_post, start_post+left_tree_size-1)
        node.right = self.helper(inorder, postorder, node_idx+1, end_in, end_post-right_tree_size, end_post-1)
        return node