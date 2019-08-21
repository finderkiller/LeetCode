# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n == 0:
            return
        dummy = ListNode(None)
        dummy.next = head
        before = dummy
        after = dummy
        while n > 0:
            after = after.next
            n -= 1
        if after == None:
            return dummy.next
        while after.next != None:
            before = before.next
            after = after.next
        before.next = before.next.next
        return dummy.next


#recursive
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head
        self.helper(dummy, n)
        return dummy.next
    def helper(self, node, n):
        if node == None:
            return 0
        value = self.helper(node.next, n) +1
        if value == n+1:
            node.next = node.next.next
        return value
        
        