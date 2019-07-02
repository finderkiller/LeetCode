# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        current = [root]
        while len(current) != 0:
            parent = current
            value = []
            current = []
            for node in parent:
                value.append(node.val)
                if node.left != None:
                    current.append(node.left)
                if node.right != None:
                    current.append(node.right)
            result.append(value)
        return result
        
#DFS

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.helper(root, result, 0)
        return result
    def helper(self, node, result, level):
        if node == None:
            return
        if len(result) == level:
            result.append([node.val])
        else:
            result[level].append(node.val)
            
        self.helper(node.left, result, level+1)
        self.helper(node.right, result, level+1)
        
        