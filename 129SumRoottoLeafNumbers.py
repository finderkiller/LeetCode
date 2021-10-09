# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        prefix = []
        self.result = 0
        self.helper(root, prefix)
        return self.result
    def helper(self, node, prefix):
        if node == None:
            return
        prefix.append(node.val)
        if node.left == None and node.right == None:
            self.result += int(''.join(map(str,prefix)))
            prefix.pop()
            return
        self.helper(node.left, prefix)
        self.helper(node.right, prefix)
        prefix.pop()
        

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return
        collection = []
        return self.helper(collection, root)
        
    def helper(self, collection, node):
        if not node:
            return 0
        collection.append(node.val)
        result = 0
        if not node.left and not node.right:
            result = int("".join(map(str, collection)))
            collection.pop()
            return result
        result += self.helper(collection, node.left)
        result += self.helper(collection, node.right)
        collection.pop()
        return result