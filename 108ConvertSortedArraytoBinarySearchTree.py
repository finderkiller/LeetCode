# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return 
        return self.helper(0, len(nums)-1, nums)
    def helper(self, start, end, nums):
        if start > end:
            return
        mid = start + (end-start)//2
        node = TreeNode(nums[mid])
        node.left = self.helper(start, mid-1, nums)
        node.right = self.helper(mid+1, end, nums)
        return node