"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        if not root:
            return 0
        self.max_diameter = 0
        self.getHeight(root)
        return self.max_diameter
        
    def getHeight(self, node):
        table = []
        for child in node.children:
            table.append(self.getHeight(child))
        max_length = 0
        second_max_length = 0
        if len(table) > 0:
            max_length = max(table)
            table.remove(max_length)
        if len(table) > 0:
            second_max_length = max(table)
        self.max_diameter = max(self.max_diameter, max_length+second_max_length)
        return max_length+1
            
        