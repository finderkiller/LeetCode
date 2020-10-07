# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        cur = head
        while cur != None and cur.next != None:
            if cur.val == cur.next.val:
                while cur != None and cur.val == pre.next.val:
                    cur = cur.next
                pre.next = cur
                continue
            pre = cur
            cur = cur.next
        return dummy.next
        