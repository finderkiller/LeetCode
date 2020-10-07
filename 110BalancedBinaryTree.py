# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        leftHeight = self.checkHeight(root.left)
        rightHeight = self.checkHeight(root.right)
        if abs(leftHeight-rightHeight) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)        
    def checkHeight(self, node):
        if node == None:
            return 0
        return max(self.checkHeight(node.left), self.checkHeight(node.right))+1
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.getHeight(root) != -sys.maxsize-1
    
    def getHeight(self, node):
        if node == None:
            return True
        leftHeight = self.getHeight(node.left)
        if leftHeight == -sys.maxsize-1:
            return leftHeight
        rightHeight = self.getHeight(node.right)
        if rightHeight == -sys.maxsize-1:
            return rightHeight
        
        diff = abs(leftHeight-rightHeight)
        if diff > 1:
            return -sys.maxsize-1
        return max(leftHeight, rightHeight)+1
        
# using global member
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.is_balanced = True
        self.getHeight(root)
        return self.is_balanced
        
    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        if not self.is_balanced:
            return
        if abs(left-right) > 1:
            self.is_balanced = False
            return
        return max(left, right)+1
        