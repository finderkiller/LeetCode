#using extra space
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = head
        fast = head
        stack = []
        while fast != None and fast.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast != None:
            slow = slow.next
        while slow != None:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True

# using recursive
class Result:
    def __init__(self, node, result):
        self.node = node
        self.result = result
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        cur = head
        while cur!= None:
            cur=cur.next
            length+=1
        result = self.helper(head, length)
        return result.result
    def helper(self, node, length):
        if length == 0:
            return Result(node, True)
        if length == 1:
            return Result(node.next, True)
        forward = self.helper(node.next, length-2)
        if forward.result == False:
            return forward
        if node.val != forward.node.val:
            return Result(forward.node, False)
        return Result(forward.node.next, True)