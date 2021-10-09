#sol1: step by step clear all leaf nodes, using postorder in each step
#time: O(nlogn), space: O(n), depth: O(logn)
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        dummy_head = TreeNode(0)
        dummy_head.left = root
        while dummy_head.left:
            result.append(self.helper(dummy_head)[0])
        return result
        
    def helper(self, node):
        if not node:
            return ([], False)
        if node.left == None and node.right == None:
            return ([node.val], True)
        left_leaves, is_left_leaves = self.helper(node.left)
        right_leaves, is_right_leaves = self.helper(node.right)
        if is_left_leaves:
            node.left = None
        if is_right_leaves:
            node.right = None
        return (left_leaves + right_leaves, False)

#sol2: postorder DFS, then clear after collection
#time: O(n), space: O(n), depth: O(logn)
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.helper(root, result)
        return result
        
    def helper(self, node, result):
        if not node:
            return 0
        left_height = self.helper(node.left, result)
        right_height = self.helper(node.right, result)
        cur_height = max(left_height, right_height)
        if len(result) == cur_height:
            result.append([])
        result[cur_height].append(node.val)
        node.left = None
        node.right = None
        return cur_height+1