class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        prev = None
        cur = head
        while cur != None:
            nextStart = cur.next
            cur.next = prev
            prev = cur
            cur = nextStart
        return prev

#! recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return self.reverse(head, None)
    def reverse(self, node, prev):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.reverse(n, node)