#BFS, two queue, time:O(n), space:O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            child_list = []
            result.append(queue[-1].val)
            for node in queue:
                if node.left:
                    child_list.append(node.left)
                if node.right:
                    child_list.append(node.right)
            queue = child_list
        return result