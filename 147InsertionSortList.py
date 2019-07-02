# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy = ListNode(None)
        dummy.next = head
        cur = head.next
        head.next = None
        while cur != None:
            nextStart = cur.next
            cur.next == None
            insert_ptr = dummy
            while insert_ptr.next != None and insert_ptr.next.val <= cur.val:
                insert_ptr = insert_ptr.next
            cur.next = insert_ptr.next
            insert_ptr.next = cur
            cur = nextStart
        return dummy.next
                
            
        