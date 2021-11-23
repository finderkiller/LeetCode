class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.cover = {None}
        self.helper(root, None)
        return self.result
        
    def helper(self, node, parent):
        if not node:
            return
        self.helper(node.left, node)
        self.helper(node.right, node)
        if (parent == None and node not in self.cover) or node.left not in self.cover or node.right not in self.cover:
            self.cover.update({node, parent, node.left, node.right})
            self.result+=1