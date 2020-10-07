# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        length = self.length(head)
        self.head = head
        return self.helper(0, length-1)
    def helper(self, start, end):
        if start > end:
            return
        if not self.head:
            return
        mid = start + (end-start)//2
        tree_node = TreeNode(None)
        tree_node.left = self.helper(start, mid-1)
        tree_node.val = self.head.val
        self.head = self.head.next
        tree_node.right = self.helper(mid+1, end)
        return tree_node
        
    def length(self, head):
        length = 0
        while head != None:
            length += 1
            head = head.next
        return length