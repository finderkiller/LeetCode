class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node.right:
            return self.leftmost(node.right)
        while node.parent and node.parent.right == node:
                node = node.parent
        return node.parent
                
            
    def leftmost(self, node):
        if not node or not node.left:
            return node
        return self.leftmost(node.left)