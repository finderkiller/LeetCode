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
        length = 0
        cur = head
        while cur != None:
            cur = cur.next
            length += 1
        self.head = head
        return self.helper(0, length-1)
        
    def helper(self, start, end):
        if start > end:
            return None
        if self.head == None:
            return None
        mid = start + (end-start)//2
        node = TreeNode(None)
        node.left = self.helper(start, mid-1)
        node.val = self.head.val
        self.head = self.head.next
        node.right = self.helper(mid+1, end)
        return node
        