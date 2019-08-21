# Definition for a binary tree node.
# class TreeNode:
# #Brute force, O(nlogn)
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        left = self.helper(root.left)
        right = self.helper(root.right)
        result = max(root.val, root.val+left, root.val+right, root.val+left+right)
        if root.left:
            result = max(result, self.maxPathSum(root.left))
        if root.right:
            result = max(result, self.maxPathSum(root.right))
        return result
        
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        return max(node.val, node.val+left, node.val+right)

#O(n)
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = -sys.maxsize-1
        self.helper(root)
        return self.max
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        self.max = max(self.max, node.val, node.val+left, node.val+right, node.val+left+right)
        return max(node.val, node.val+left, node.val+right)