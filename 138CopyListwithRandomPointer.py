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
        table = {}
        return self.helper(head, table)
    def helper(self, node, table):
        if not node:
            return None
        if node.val in table:
            return table[node.val]
        new_node = Node(node.val, None, None)
        table[node.val] = new_node
        new_node.next = self.helper(node.next, table)
        new_node.random = self.helper(node.random, table)
        return table[node.val]
        