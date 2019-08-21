#brute force O(nlogn)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        dia = self.getheight(root.left)
        dia += self.getheight(root.right)
        return max(dia, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    def getheight(self, node):
        if not node:
            return 0
        left = self.getheight(node.left)
        right = self.getheight(node.right)
        return max(left, right) + 1

#DFS O(n)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxdia = 0
        self.helper(root)
        return self.maxdia
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        self.maxdia = max(self.maxdia, left + right)
        return max(left, right)+1