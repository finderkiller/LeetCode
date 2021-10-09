# time: O(n)
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ptr_p = p
        ptr_q = q
        length_p = 0
        length_q = 0
        while ptr_p:
            ptr_p = ptr_p.parent
            length_p += 1
        while ptr_q:
            ptr_q = ptr_q.parent
            length_q += 1
        ptr_p = p
        ptr_q = q
        diff = abs(length_p - length_q)
        if length_p > length_q:
            while diff > 0:
                ptr_p = ptr_p.parent
                diff -= 1
        elif length_q > length_p:
            while diff > 0:
                ptr_q = ptr_q.parent
                diff -= 1
        while ptr_p != ptr_q:
            ptr_p = ptr_p.parent
            ptr_q = ptr_q.parent
        
        return ptr_p
            
        