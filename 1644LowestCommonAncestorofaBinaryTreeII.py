# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
brute force: O(nlogm)

duplicated comuptation for each finding -> enchance
O(n), return node and is_ancestor data, Ret(node, is_ancestor)
   
    
    

    
# handle:
    0. left = helper(node.left), right = helper(node.right)
    1. if left or right is_ancestor, just return node
    2. if left has node and not is_ancestor and right has node and not is_ancestor
        return (node, True)
    2. node == p or node == q
    3. if left has node but right not has node, meaning find p or q only
        return (node, False)
    4. if left and right do not have node and this node not p or q
        return (Null, False)
    5. on root node, if get ret.is_ancestor == False, meaning there is no ancestor in this tree, meaning that do not find p or q or both
"""

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
            return
        ret = self.helper(root, p, q)
        if not ret.is_ancestor:
            return
        else:
            return ret.node
        
    def helper(self, node, p, q):
        if not node:
            return Ret(None, False)
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)
        if left.is_ancestor:
            return left
        if right.is_ancestor:
            return right
        if right.node and left.node:
            return Ret(node, True)
        if node == p or node == q:
            return Ret(node, True if right.node or left.node else False)
        if right.node:
            return right
        if left.node:
            return left
        return Ret(None, False)