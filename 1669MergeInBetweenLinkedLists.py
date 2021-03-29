# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = list1
        point_a = dummy
        point_b = list1
        list2_tail = list2
        
        while list2_tail and list2_tail.next != None:
            list2_tail = list2_tail.next
        
        while a > 0:
            if point_a == None:
                return
            point_a = point_a.next
            a -= 1
        while b > -1:
            if point_b == None:
                return
            point_b = point_b.next
            b -= 1
        
        point_a.next = list2
        list2_tail.next = point_b
        return dummy.next