# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        length =self.getLength(head)
        k = k % length
        p1 = p2 = head
        while k > 0:
            p2 = p2.next
            k -= 1
        while p2 and p2.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = head
        head = p1.next
        p1.next = None
        return head
            
        
    def getLength(self, cur):
        if not cur:
            return 0
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length