# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lengthA = 0
        lengthB = 0
        curA = headA
        curB = headB
        
        while curA != None:
            lengthA += 1
            curA = curA.next
        while curB != None:
            lengthB += 1
            curB = curB.next
        if curA != curB:
            return None
        diff = abs(lengthA- lengthB)
        curA = headA
        curB = headB
        if lengthA > lengthB:
            while diff != 0:
                curA = curA.next
                diff -= 1
        else:
            while diff != 0:
                curB = curB.next
                diff -= 1
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA
        