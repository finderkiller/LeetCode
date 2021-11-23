#O(n)
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

#O(logn ^ 2)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftHeight = self.getLeftHeight(root.left)
        rightHeight = self.getLeftHeight(root.right)
        if leftHeight == rightHeight:
            return 2**leftHeight + self.countNodes(root.right)
        else:
            return 2**rightHeight + self.countNodes(root.left)
        
    def getLeftHeight(self, node):
        if not node:
            return 0
        return 1+self.getLeftHeight(node.left)