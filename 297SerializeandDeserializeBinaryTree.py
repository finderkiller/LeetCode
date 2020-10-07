class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'x,'
        result = str(root.val) + ','
        result += self.serialize(root.left)
        result += self.serialize(root.right)
        return result
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        self.idx = 0
        self.array = data.split(',')
        return self.helper()
    def helper(self):
        if self.idx >= len(self.array):
            return
        if self.array[self.idx] == 'x':
            self.idx += 1
            return
        value = int(self.array[self.idx])
        node = TreeNode(value)
        self.idx += 1
        node.left = self.helper()
        node.right = self.helper()
        return node
        