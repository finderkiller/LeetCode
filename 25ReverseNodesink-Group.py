# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        cur = head
        while cur != None:
            if not self.is_reversible(cur, k):
                break
            rev_head, next_cur = self.reverse(None, cur, k)
            pre.next = rev_head
            cur.next = next_cur   #cur is rev_tail
            pre = cur
            cur = next_cur
        return dummy.next
    
    def reverse(self, pre, cur, k):
        while k > 0:
            next_cur = cur.next
            cur.next = pre
            pre = cur
            cur = next_cur
            k -= 1
        return (pre, cur)
        
    def is_reversible(self, cur, k):
        while cur != None and k > 0:
            cur = cur.next
            k -= 1
        return k == 0