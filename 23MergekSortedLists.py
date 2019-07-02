# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
             return None
        return self.sort(lists, 0, len(lists)-1)
    
    def sort(self, lists, low, high):
        if low >= high:
            return lists[low]
        mid = (high-low)//2 + low
        l1 = self.sort(lists, low, mid)
        l2 = self.sort(lists, mid+1, high)
        return self.merge(l1, l2)
        
    def merge(self, l1, l2):    #! merge two sorted list
        if l1 == None:
             return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        l2.next = self.merge(l1, l2.next)
        return l2