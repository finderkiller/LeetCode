# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fast = head
        slow = head
        has_cycle = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break
        if not has_cycle:
            return None
        
        slow = head
        while not (slow is fast):
            slow = slow.next
            fast = fast.next
        return slow
            
        