#time: O(1), space: O(1)
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        #left
        if rec1[0] >= rec2[2]:
            return False
        #right
        if rec1[2] <= rec2[0]:
            return False
        #down
        if rec1[1] >= rec2[3]:
            return False
        #up
        if rec1[3] <= rec2[1]:
            return False
        return True