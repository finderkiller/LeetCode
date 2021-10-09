#recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.helper(root, result)
        return result
    def helper(self, node, result):
        if node == None:
            return
        self.helper(node.left, result)
        result.append(node.val)
        self.helper(node.right, result)

#iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        result = []
        stack = []
        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                pop_item = stack.pop()
                result.append(pop_item.val)
                current = pop_item.right
            else:
                break
        return result