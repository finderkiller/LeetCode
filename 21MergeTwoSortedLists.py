# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummyHead = ListNode(0)
        cur = dummyHead
        
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
                cur.next == None
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next
                cur.next == None
        if l1 != None:
            cur.next = l1
        elif l2 != None:
            cur.next = l2
        return dummyHead.next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2            