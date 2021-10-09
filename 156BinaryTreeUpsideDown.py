# time: O(logn)
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.helper(root)
        return self.new_root
    def helper(self, node):
        if not node:
            return
        parent = self.helper(node.left)
        if not parent:
            self.new_root = node
            return node
        parent.right = node
        node.left = None
        parent.left = node.right
        node.right = None
        return node
        