# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.result = []
        self.helper(root, target, K)
        return self.result
        
    def helper(self, node, target, K):
        if not node:
            return -1
        if node == target:
            self.subtree_add(node, K)
            return 0
        forward = self.helper(node.left, target, K)
        if forward != -1:
            distance = 1 + forward
            if distance == K:
                self.result.append(node.val)
            self.subtree_add(node.right, K-distance-1)
            return distance
        forward = self.helper(node.right, target, K)
        if forward != -1:
            distance = 1 + forward
            if distance == K:
                self.result.append(node.val)
            self.subtree_add(node.left, K-distance-1)
            return distance
        return -1
    
    
    def subtree_add(self, node, distance):
        if not node:
            return 
        if distance == 0:
            self.result.append(node.val)
            return
        self.subtree_add(node.left, distance-1)
        self.subtree_add(node.right, distance-1)
        