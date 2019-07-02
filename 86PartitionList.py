# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        listlowhead = None
        listlowtail = None
        listhighhead = None
        listhightail = None
        if head == None:
            return None
        
        cur = head
        while cur != None:
            if cur.val < x:
                if listlowhead == None:
                    listlowhead = ListNode(cur.val)
                    listlowtail = listlowhead
                else:
                    listlowtail.next = ListNode(cur.val)
                    listlowtail = listlowtail.next
            else:
                if listhighhead == None:
                    listhighhead = ListNode(cur.val)
                    listhightail = listhighhead
                else:
                    listhightail.next = ListNode(cur.val)
                    listhightail = listhightail.next
            cur = cur.next
        
        if (listlowtail != None):
            listlowtail.next = listhighhead
            return listlowhead
        else:
            return listhighhead
