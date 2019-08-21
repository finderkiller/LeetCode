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
        if not self.find(root,p) or not self.find(root,q):
            return None
        return self.helper(root, p, q)
    def helper(self, root, p, q):
        if root == None:
            return None
        if root == p:
            return p
        if root == q:
            return q
        p_in_left = self.find(root.left, p)
        q_in_left = self.find(root.left, q)
        if p_in_left != q_in_left:
            return root
        if p_in_left and q_in_left:
            return self.helper(root.left, p, q)
        else:
            return self.helper(root.right, p, q)
    
    def find(self, node, p):
        if not node:
            return False
        if node == p:
            return True
        return self.find(node.right, p) or self.find(node.left, p)


# return node and is_ancestor
class Result:
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
        result = self.helper(root, p, q)
        return result.node if result.is_ancestor else None
        
    def helper(self, node, p, q):
        if not node:
            return Result(None, False)
        if node == p and node == q:
            return Result(node, True)
        
        left_result = self.helper(node.left, p, q)
        if left_result.is_ancestor:
            return left_result
        
        right_result = self.helper(node.right, p, q)
        if right_result.is_ancestor:
            return right_result
        
        if left_result.node and right_result.node:
            return Result(node, True)
        
        if node == p or node == q:
            result = left_result.node != None or right_result.node != None
            return Result(node, result)
        if left_result.node:
            return left_result
        if right_result.node:
            return right_result
        else:
            return Result(None, False)