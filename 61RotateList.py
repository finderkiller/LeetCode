# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        length = self.length(head)
        if length == 1 or length == k:
            return head
        if k > length:
            k = k % length
        p1 = p2 = head
        for idx in range(k):
            p2 = p2.next
        
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        p2.next = head
        head = p1.next
        p1.next = None
        return head
            
    def length(self,node):
        if node == None:
            return 0
        return self.length(node.next)+1
