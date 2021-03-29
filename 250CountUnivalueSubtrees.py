# O(nlogn)
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 0
        if self.helper(root.left, root.val) and self.helper(root.right, root.val):
            result += 1
        result += self.countUnivalSubtrees(root.left) + self.countUnivalSubtrees(root.right)
        return result
        
    def helper(self, node, value):
        if not node:
            return True
        if node.val != value:
            return False
        if not self.helper(node.left, value):
            return False
        if not self.helper(node.right, value):
            return False
        return True
        