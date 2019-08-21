#two way
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head
        prev_start = dummy
        end = dummy
        while m-1 > 0:
            prev_start = prev_start.next
            m = m-1
        while n > 0:
            end = end.next
            n = n-1
        nextStart = end.next
        end.next = None
        
        prev_start.next = self.reverse(nextStart, prev_start.next)
        return dummy.next
        
    def reverse(self, prev, cur):
        if cur == None:
            return prev
        n = cur.next
        cur.next = prev
        return self.reverse(cur, n)

# one way
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        cur = head
        prev_start = None
        tail = None
        while m > 1:
            prev = cur 
            cur = cur.next
            m -= 1
            n -= 1
            
        prev_start = prev
        tail = cur

        while n > 0:
            nextStart = cur.next
            cur.next=prev
            prev = cur
            cur = nextStart
            n -= 1
        prev_start.next = prev
        tail.next = cur
        return dummy.next