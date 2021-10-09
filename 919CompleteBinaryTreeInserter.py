# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""          10
        1           0
    2       3    8.   9
 4     5 6.   7  
 
# level order travese, using queue


"""
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        

    def insert(self, val: int) -> int:
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            child_list = []
            for node in queue:
                if node.left:
                    child_list.append(node.left)
                else:
                    node.left = TreeNode(val)
                    return node.val
                if node.right:
                    child_list.append(node.right)
                else:
                    node.right = TreeNode(val)
                    return node.val
            queue = child_list
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()