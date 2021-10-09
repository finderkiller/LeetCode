#time: O(n), extra space:O(n), callstack: O(logn)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = self.inorder(root)
        return result[k-1]
        
    def inorder(self, node):
        if not node:
            return []
        result = []
        result += self.inorder(node.left)
        result += [node.val]
        result += self.inorder(node.right)
        return result
#time: O(k), extra space: O(1), callstack: O(logn)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.result = 0
        self.index = 0
        self.helper(root, k)
        return self.result
        
    def helper(self, node, k):
        if not node:
            return
        if self.helper(node.left, k):
            return True
        self.index += 1
        if self.index == k:
            self.result = node.val
            return True
        if self.helper(node.right, k):
            return True

# follow up: insert and delete frequently, remember left.size in each node