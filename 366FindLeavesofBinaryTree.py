#sol1: delete old leaves first, step by step clear all leaf nodes, using postorder in each step
#time: O(nlogn), space: O(n), depth: O(logn)
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        result = []
        collection = []
        if self.helper(root, collection):
            result.append(collection)
            return result
        result.append(collection)
        result += self.findLeaves(root)
        return result
    
    def helper(self, node, collection):
        if not node:
            return False
        if not node.left and not node.right:
            collection.append(node.val)
            return True
        left_is_leaf = self.helper(node.left, collection)
        right_is_leaf = self.helper(node.right, collection)
        if left_is_leaf:
            node.left = None
        if right_is_leaf:
            node.right = None
        return False

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        result = []
        root_is_leaf = False
        while not root_is_leaf:
            collection = []
            root_is_leaf = self.postorder(root, collection)
            result.append(collection)
        return result
    
    def postorder(self, node, collection):
        if not node:
            return False
        if not node.left and not node.right:
            collection.append(node.val)
            return True
        left_is_leaf = self.postorder(node.left, collection)
        right_is_leaf = self.postorder(node.right, collection)
        if left_is_leaf:
            node.left = None
        if right_is_leaf:
            node.right = None
        return False

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, root, result):
        collection = []
        root_is_leaf = self.postorder(root, collection)
        result.append(collection)
        if root_is_leaf:
            return
        self.helper(root, result)
    
    def postorder(self, node, collection):
        if not node:
            return False
        if not node.left and not node.right:
            collection.append(node.val)
            return True
        left_is_leaf = self.postorder(node.left, collection)
        right_is_leaf = self.postorder(node.right, collection)
        if left_is_leaf:
            node.left = None
        if right_is_leaf:
            node.right = None
        return False



#sol2: delete new leaves first, postorder DFS, then clear after collection
#time: O(n), space: O(n), depth: O(logn)
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.result = []
        self.postorder(root)
        return self.result
        
    def postorder(self, node):
        if not node:
            return 0
        left_height = self.postorder(node.left)
        right_height = self.postorder(node.right)
        current_height = max(left_height, right_height)
        if current_height == len(self.result):
            self.result.append([])
        self.result[current_height].append(node.val)
        node.left = None
        node.right = None
        return current_height + 1