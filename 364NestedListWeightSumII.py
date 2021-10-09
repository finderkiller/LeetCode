# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

#O(n)
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0
        self.max_depth = self.findMaxDepth(nestedList, 1)
        self.result = 0
        self.helper(nestedList, 1)
        return self.result
        
    def findMaxDepth(self, nestedList, level):
        max_depth = level
        for data in nestedList:
            if not data.isInteger():
                max_depth = max(max_depth, self.findMaxDepth(data.getList(), level+1))
        return max_depth
    
    def helper(self, nestedList, level):
        for data in nestedList:
            if data.isInteger():
                self.result += data.getInteger() * (self.max_depth-level+1)
            else:
                self.helper(data.getList(), level+1)
        