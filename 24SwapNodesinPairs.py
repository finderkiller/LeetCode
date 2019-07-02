# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        pre = dummy
        while cur != None and cur.next != None:
            nextStart = cur.next.next        #!remember using nextStart save the start of the next iteration
            pre.next = cur.next
            cur.next.next = cur
            cur.next = nextStart
            pre = cur
            cur = cur.next
        return dummy.next
        