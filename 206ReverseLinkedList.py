#! iteration
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        cur = None
        while head != None:
            temp = head.next
            head.next = cur
            cur = head
            if temp == None:
                return head
            head = temp
        return head

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