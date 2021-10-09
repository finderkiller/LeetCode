"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ",x"
        result = ',' + str(root.val)
        result += ',' + str(len(root.children))
        for child in root.children:
            result += self.serialize(child)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return
        array = data.split(',')[1:]
        self.index = 0
        return self.helper(array)
        
    def helper(self, array):
        if self.index >= len(array):
            return
        value = array[self.index]
        self.index += 1
        if value == 'x':
            return
        node = Node(int(value), [])
        count = int(array[self.index])
        self.index += 1
        while count > 0:
            node.children.append(self.helper(array))
            count -= 1
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))