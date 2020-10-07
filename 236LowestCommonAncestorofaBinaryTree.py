class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not self.isCover(root, p):
            return None
        if not self.isCover(root, q):
            return None
        if self.isCover(p, q):
            return p
        if self.isCover(q, p):
            return q
        return self.helper(root, p, q)
        
        
    def helper(self, node, p, q):
        if not node:
            return None
        p_in_left = self.isCover(node.left, p)
        q_in_left = self.isCover(node.left, q)
        if p_in_left and q_in_left:
            return self.helper(node.left, p, q)
        elif not p_in_left and not q_in_left:
            return self.helper(node.right, p, q)
        else:
            return node
        
    def isCover(self, node, target):
        if not node:
            return False
        if node == target:
            return True
        return self.isCover(node.left, target) or self.isCover(node.right, target)


# return node and is_ancestor
class Ret:
    def __init__(self, node, is_ancestor):
        self.node = node
        self.is_ancestor = is_ancestor
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        ret = self.helper(root, p, q)
        return ret.node if ret.is_ancestor else None
    
    def helper(self, node, p, q):
        if not node:
            return Ret(None, False)
        if node == p and node == q:
            return Ret(node, True)
        
        left_ret = self.helper(node.left, p, q)
        right_ret = self.helper(node.right, p, q)
        
        if left_ret.is_ancestor:
            return left_ret
        if right_ret.is_ancestor:
            return right_ret
        if left_ret.node and right_ret.node:
            return Ret(node, True)
        
        if node == p or node == q:
            is_ancestor = left_ret.node or right_ret.node
            return Ret(node, is_ancestor)
        if left_ret.node:
            return left_ret
        if right_ret.node:
            return right_ret
        return Ret(None, False)