# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return 
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur != None:          
            next_start = self.findNextStart(cur, k)
            pre.next = self.reverse(cur, next_start,k)
            pre = cur
            cur = next_start
        return dummy.next
    
    def findNextStart(self, cur, k):
        if cur == None:
            return None
        if k == 0:
            return cur
        return self.findNextStart(cur.next, k-1)
        
    def reverse(self, cur, next_start, k):
        if cur == None:
            return
        count = 0
        tmp = cur
        while tmp != None and count !=k:
            count += 1
            tmp = tmp.next
        if count != k:
            return cur
        ret = self.helper(cur, next_start, k)
        return ret
    def helper(self, cur, prev, k):
        if k == 0:
            return prev
        n = cur.next
        cur.next = prev
        return self.helper(n, cur, k-1)
        