# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.helper(l1, l2, 0)
    def helper(self, l1, l2, carry):
        if not l1 and not l2 and carry == 0:
            return None
        sum = carry
        if l1:
            sum += l1.val
        if l2:
            sum += l2.val
        new_node = ListNode(sum%10)
        new_node.next = self.helper(l1.next if l1 else None, l2.next if l2 else None, sum//10)
        return new_node
        