# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return []
        length_pre = len(preorder)
        length_in = len(inorder)
        if length_pre != length_in:
            return []
        return self.helper(preorder, inorder, 0, length_pre-1, 0, length_in-1)
    def helper(self, preorder, inorder, start_pre, end_pre, start_in, end_in):
        if start_in > end_in or start_pre > end_pre:
            return None
        node = TreeNode(preorder[start_pre])
        node_idx = -1
        for idx in range(start_in, end_in+1):
            if inorder[idx] == node.val:
                node_idx = idx
                break
        left_tree_size = node_idx-start_in
        right_tree_size = end_in-node_idx
        node.left = self.helper(preorder, inorder, start_pre+1, start_pre+left_tree_size, start_in, node_idx-1)
        node.right = self.helper(preorder, inorder, end_pre-right_tree_size+1, end_pre, node_idx+1, end_in)
        return node
        