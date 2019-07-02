# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.sort(head)
    def sort(self, head):
        if not head:
            return None
        if not head.next:
            return head
        pre = self.findMid(head)
        mid = pre.next
        pre.next = None
        l1 = self.sort(head)
        l2 = self.sort(mid)
        return self.merge(l1, l2)
        
    def findMid(self, head):
        if not head:
            return None
        slow = head
        fast = head
        pre = None
        while fast != None and fast.next != None:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        return pre
    def merge(self, first, second):
        if not first:
            return second
        if not second:
            return first
        if first.val < second.val:
            first.next = self.merge(first.next, second)
            return first
        else:
            second.next = self.merge(first, second.next)
            return second
        