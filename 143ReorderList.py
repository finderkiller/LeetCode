# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        first = head
        second = self.separateTwoList(head)
        second = self.reverseList(None, second)
        self.insert(first, second)
        
    def separateTwoList(self, head):
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        ret = slow.next
        slow.next = None
        return ret
    def reverseList(self, prev, cur):
        if cur == None:
            return prev
        nextStart = cur.next
        cur.next = prev
        return self.reverseList(cur, nextStart)
    def insert(self, first, second):
        while first and second:
            nextFirstStart = first.next
            first.next = second
            nextSecondStart = second.next
            second.next = nextFirstStart
            first = nextFirstStart
            second = nextSecondStart
            
        
        