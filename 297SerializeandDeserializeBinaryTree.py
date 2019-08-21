class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#,"
        result = str(root.val) + ","
        result += self.serialize(root.left)
        result += self.serialize(root.right)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.idx = 0
        nums = data.split(",")
        return self.helper(nums)
    
    def helper(self, nums):
        if self.idx >= len(nums):
            return
        if nums[self.idx] == "#":
            return
        node = TreeNode(int(nums[self.idx]))
        self.idx += 1
        node.left = self.helper(nums)
        self.idx += 1
        node.right = self.helper(nums)
        return node