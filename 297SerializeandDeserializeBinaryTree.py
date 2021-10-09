# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ',x'
        result = ',' + str(root.val)
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
        array = data.split(',')[1:-1]
        self.start = 0
        return self.helper(array)
        
    def helper(self, array):
        if self.start >= len(array):
            return
        value = array[self.start]
        self.start += 1
        if value == 'x':
            return
        node = TreeNode(int(value))
        node.left = self.helper(array)
        node.right = self.helper(array)
        return node
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))