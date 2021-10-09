# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.node_list = []
        self.vals_list = []
        self.inorder(root)
        self.vals_list.sort()
        for idx in range(len(self.node_list)):
            self.node_list[idx].val = self.vals_list[idx]
        return root
    
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.node_list.append(node)
        self.vals_list.append(node.val)
        self.inorder(node.right)

#sol2: inorder twice
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.array = []
        self.inorder(root)
        self.array.sort()
        self.index = 0
        self.recover(root)
        
        
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.array.append(node.val)
        self.inorder(node.right)
    
    def recover(self, node):
        if not node:
            return
        self.recover(node.left)
        node.val = self.array[self.index]
        self.index += 1
        self.recover(node.right)
        