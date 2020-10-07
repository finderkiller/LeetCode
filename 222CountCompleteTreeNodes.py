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
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        h = self.getheight(root)
        right_height = self.getheight(root.right)
        if h-1 == right_height:
            return 2**(h-1) + self.countNodes(root.right)
        else:
            return 2**(right_height)+self.countNodes(root.left)
    def getheight(self, node):
        if not node:
            return 0
        return 1+self.getheight(node.left)