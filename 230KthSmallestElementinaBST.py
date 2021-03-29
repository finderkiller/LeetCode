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
        self.value = 0
        self.k = k
        self.inorder(root)
        return self.value
        
    def inorder(self, node):
        if not node:
            return False
        if self.inorder(node.left):
            return True
        self.k -= 1
        if self.k == 0:
            self.value = node.val
            return True
        if self.inorder(node.right):
            return True
        return False