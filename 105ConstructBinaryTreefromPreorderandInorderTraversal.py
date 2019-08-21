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
        