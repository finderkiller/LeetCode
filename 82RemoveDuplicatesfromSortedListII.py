# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        while pre != None:
            current = pre.next
            hasDu = False
            while current != None and current.next != None:
                if current.val == current.next.val:
                    hasDu = True
                    current.next = current.next.next
                else:
                    break
            if hasDu:
                pre.next =current.next
            else:
                pre = current
                
        return dummy.next
        