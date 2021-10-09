#brute force, time: O(n), depth:O(logn)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        result = 0
        if root.val >= L and root.val <= R:
            result += root.val
        result += self.rangeSumBST(root.left, L, R)
        result += self.rangeSumBST(root.right, L, R)
        return result

#time: O(n), space: O()
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        result = 0
        if root.val >= L and root.val <= R:
            result += root.val
        if L < root.val:
            result += self.rangeSumBST(root.left, L, R)
        if R > root.val:
            result += self.rangeSumBST(root.right, L, R)
        return result