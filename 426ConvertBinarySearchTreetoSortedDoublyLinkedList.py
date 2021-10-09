#time: O(n), space: O(logn)
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        self.first = None
        self.last = None
        self.helper(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first
        
    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        if self.last:
            self.last.right = node
            node.left = self.last
        else:
            self.first = node
        self.last = node
        self.helper(node.right)