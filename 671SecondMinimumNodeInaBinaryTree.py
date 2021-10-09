# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.array = list(set(self.inorder(root)))
        import heapq
        heap = []
        for value in self.array:
            heapq.heappush(heap, 0-value)
            if len(heap) > 2:
                heapq.heappop(heap)
        return 0-heap[0] if len(heap) == 2 else -1
        
        
    def inorder(self, node):
        if not node:
            return []
        result = []
        result += self.inorder(node.left)
        result.append(node.val)
        result += self.inorder(node.right)
        return result