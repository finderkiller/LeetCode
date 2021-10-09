# if nodes have parent
def leftmost(node):
    if node == None:
        return None
    while(node.left != None):
        node = node.left
    return node

def successor(node):
    if node == None:
        return None
    if node.right != None:
        return leftmost(node.right)
    cur = node
    while(cur.parent != None and cur.parent.right = cur):
        cur = cur.parent
    return cur.parent


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.pre_node = None
        self.result = None
        self.inorder(root, p)
        return self.result
        
    def inorder(self, node, p):
        if not node:
            return
        self.inorder(node.left, p)
        if self.pre_node == p:
            self.result = node
        self.pre_node = node
        self.inorder(node.right, p)
        