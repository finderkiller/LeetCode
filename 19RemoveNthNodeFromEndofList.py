# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        dummy = ListNode(None)
        dummy.next = head
        first = dummy
        second = dummy
        for idx in range(n):
            second = second.next
        while second != None and second.next != None:
            first = first.next
            second = second.next
        if second == None:
            return
        first.next = first.next.next
        return dummy.next


#recursive
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        dummy = ListNode(None)
        dummy.next = head
        self.helper(dummy, n)
        return dummy.next
    def helper(self, node, n):
        if not node.next:
            return 1
        value = self.helper(node.next, n)
        if value == n:
            node.next = node.next.next
        return value+1