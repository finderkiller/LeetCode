
#using table, so need to start and end that idx could be the same
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        length_post = len(postorder)
        length_in = len(inorder)
        if length_post != length_in:
            return None
        self.table = {}
        for idx, value in enumerate(inorder):
            self.table[value] = idx
        return self.helper(inorder, postorder, 0, length_in-1, 0, length_post-1)
    def helper(self, inorder, postorder, in_start, in_end, post_start, post_end):
        if in_start > in_end or post_start > post_end:
            return
        value = postorder[post_end]
        index = self.table[value]
        leftsize = index-in_start
        node = TreeNode(value)
        node.left = self.helper(inorder, postorder, in_start, index-1, post_start, post_start+leftsize-1)
        node.right = self.helper(inorder, postorder, index+1, in_end, post_start+leftsize, post_end-1)
        return node

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        length_post = len(postorder)
        length_in = len(inorder)
        if length_post != length_in:
            return None
        return self.helper(inorder, postorder)
    def helper(self, inorder, postorder):
        if not inorder or not postorder:
            return
        value = postorder[-1]
        leftsize = 0
        for data in inorder:
            if data == value:
                break
            leftsize += 1
        node = TreeNode(value)
        node.left = self.helper(inorder[:leftsize], postorder[:leftsize])
        node.right = self.helper(inorder[leftsize+1:], postorder[leftsize:len(postorder)-1])
        return node
        