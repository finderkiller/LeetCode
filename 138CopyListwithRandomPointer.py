"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.table = {}
        return self.helper(head)
    def helper(self, node):
        if not node:
            return
        if (node.val, node.next) in self.table:
            return self.table[(node.val, node.next)]
        new_node = Node(node.val, None, None)
        self.table[(node.val, node.next)] = new_node
        new_node.next = self.helper(node.next)
        new_node.random = self.helper(node.random)
        return new_node