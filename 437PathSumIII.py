#Brute force
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        count = self.helper(root, sum)
        count += self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return count
        
    def helper(self, node, sum):
        if not node:
            return 0
        totalSum = 0
        if sum-node.val == 0:
            totalSum += 1
        totalSum += self.helper(node.left, sum-node.val)
        totalSum += self.helper(node.right, sum-node.val)
        return totalSum
#Hash Table, O(n), space:O(logn)
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
        
    def helper(self, node, prev_sum, target):
        if not node:
            return 0
        currentSum = prev_sum + node.val
        total = self.table.get(currentSum-target, 0)
        if currentSum == target:
            total += 1
        self.maintainSumTable(currentSum, 1)
        total += self.helper(node.left, currentSum, target)
        total += self.helper(node.right, currentSum, target)
        self.maintainSumTable(currentSum, -1)
        return total
    def maintainSumTable(self, amount, delta):
        if amount not in self.table:
            self.table[amount] = delta
        else:
            self.table[amount] += delta