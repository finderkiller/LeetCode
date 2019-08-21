# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        collect = []
        result = []
        self.helper(collect, root, sum, result)
        return result
    def helper(self, collect, node, target, result):
        if node == None:
            return
        if node.left == None and node.right == None and node.val == target:
            new_list = list(collect)
            new_list.append(target)
            result.append(new_list)
            return
        collect.append(node.val)
        self.helper(collect, node.left, target-node.val, result)
        self.helper(collect, node.right, target-node.val, result)
        collect.pop()