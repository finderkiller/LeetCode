#sol1: preorder compare, time: O(m+n), space: O(m+n)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        strings = ',' + self.preorder(s)
        stringt = ',' + self.preorder(t)
        
        return stringt in strings
        
    def preorder(self, node):
        if not node:
            return 'x,'
        string = str(node.val) + ','
        string += self.preorder(node.left)
        string += self.preorder(node.right)
        return string

#sol2: recursive match, time: O(m + kn), space: O(logm+logn)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False
        if s.val == t.val and self.helper(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    def helper(self, node, target):
        if not node and not target:
            return True
        if not node or not target:
            return False
        if node.val == target.val:
            return self.helper(node.left, target.left) and self.helper(node.right, target.right)
        return False
        