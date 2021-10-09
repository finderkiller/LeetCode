# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
1. init:
    stack = []
2. next:
    while current_ptr:
        stack.append()
        current_ptr = current_ptr.left
    pop_item = stack.pop()
    ret = pop_item.val
    current_ptr = pop_item.right
    
"""

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self.current_ptr = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.current_ptr:
            self.stack.append(self.current_ptr)
            self.current_ptr = self.current_ptr.left
        pop_item = self.stack.pop()
        self.current_ptr = pop_item.right
        return pop_item.val
        
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0 or self.current_ptr


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()