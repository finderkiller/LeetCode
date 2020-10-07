#Brute force
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.helper(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
    def helper(self, node, current, target):
        if not node:
            return 0
        count = 0
        current += node.val
        if current == target:
            count = 1
        count += self.helper(node.left, current, target)
        count += self.helper(node.right, current, target)
        return count
#Hash Table, O(n), space:O(logn)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.table = {}
        return self.helper(root, 0, sum)
        
    def helper(self, node, cur_sum, target):
        if not node:
            return 0
        result = 0
        cur_sum += node.val
        if cur_sum == target:
            result += 1
        result += self.table.get(cur_sum-target, 0)
        
        self.table[cur_sum] = self.table.get(cur_sum, 0)+1
        result += self.helper(node.left, cur_sum, target)
        result += self.helper(node.right, cur_sum, target)
        self.table[cur_sum] = self.table.get(cur_sum, 0)-1
        
        return result
            