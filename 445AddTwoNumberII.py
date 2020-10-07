# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Ret:
    def __init__(self, node, carry):
        self.node = node
        self.carry = carry
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        length1 = self.getLength(l1)
        length2 = self.getLength(l2)
        
        if length1 > length2:
            l2 = self.prependZero(l2, length1-length2)
        elif length1 < length2:
            l1 = self.prependZero(l1, length2-length1)
        ret = self.helper(l1, l2)
        if ret.carry == 0:
            return ret.node
        else:
            node = ListNode(ret.carry)
            node.next = ret.node
            return node
    
    def helper(self, l1, l2):
        if not l1 and not l2:
            return Ret(None, 0)
        prev = self.helper(l1.next, l2.next)
        value = prev.carry
        value += l1.val + l2.val
        node = ListNode(value%10)
        node.next = prev.node
        return Ret(node, value//10)
        
        
    def getLength(self, cur):
        if not cur:
            return 0
        length = 0
        while cur != None:
            length += 1
            cur = cur.next
        return length
        
    def prependZero(self, l, num):
        if not l:
            return
        for idx in range(num):
            node = ListNode(0)
            node.next = l
            l = node
        return l
        