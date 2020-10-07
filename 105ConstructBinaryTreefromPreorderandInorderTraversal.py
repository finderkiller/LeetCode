# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
        if len(preorder) != len(inorder):
            return
        return self.helper(preorder, inorder)
    def helper(self, preorder, inorder):
        if not preorder or not inorder:
            return
        value = preorder[0]
        leftsize = 0
        for data in inorder:
            if data == value:
                break
            leftsize += 1
        node = TreeNode(value)
        node.left = self.helper(preorder[1:leftsize+1], inorder[:leftsize])
        node.right = self.helper(preorder[leftsize+1:], inorder[leftsize+1:])
        return node
        
#hash_table
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        if not inorder:
            return
        self.pos_table = {}
        for idx, value in enumerate(inorder):
            self.pos_table[value] = idx
        return self.helper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
    def helper(self, preorder, inorder, preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start > preorder_end or inorder_start > inorder_end:
            return
        value = preorder[preorder_start]
        node = TreeNode(value)
        index = self.pos_table[value]
        left_size = index-inorder_start
        node.left = self.helper(preorder, inorder, preorder_start+1, preorder_start+left_size, inorder_start, index-1)
        node.right = self.helper(preorder, inorder, preorder_start+left_size+1, preorder_end, index+1, inorder_end)
        return node