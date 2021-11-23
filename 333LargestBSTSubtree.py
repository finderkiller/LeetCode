# min_max, O(nlogn)
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.max_node = 0
        self.helper(root)
        return self.max_node
    def helper(self, node):
        if not node:
            return
        result = self.minmax(node, -sys.maxsize-1, sys.maxsize)
        self.max_node = max(self.max_node, result)
        self.helper(node.left)
        self.helper(node.right)
        
    def minmax(self, node, min_value, max_value):
        if not node:
            return 0
        if node.val >= max_value or node.val <= min_value:
            return -1
        left_node = self.minmax(node.left, min_value, node.val)
        right_node = self.minmax(node.right, node.val, max_value)
        if left_node == -1 or right_node == -1:
            return -1
        return left_node + right_node + 1

# Inorder, O(nlogn)
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        inorder_list = self.helper(root)
        success = True
        result = 0
        for idx in range(1, len(inorder_list)):
            if inorder_list[idx-1] >= inorder_list[idx]:
                success = False
                break
        result = len(inorder_list) if success else 0
        result = max(result, self.largestBSTSubtree(root.left),\
                     self.largestBSTSubtree(root.right))
        return result
        
    def helper(self, node):
        if not node:
            return []
        result = self.helper(node.left)
        result.append(node.val)
        result += self.helper(node.right)
        return result
    
# Inorder, O(nlogn) since each level still traverse n, n-1, n-3....
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.max_node = 0
        self.inorder(root)
        return self.max_node                
    def inorder(self, node):
        if not node:
            return []
        result = self.inorder(node.left)
        result += [node.val]
        result += self.inorder(node.right)
        success = True
        for idx in range(1, len(result)):
            if result[idx] <= result[idx-1]:
                success = False
                break
        if success:
            self.max_node = max(self.max_node, len(result))
        return result
        
#Inorder, O(n), no traverse on each level anymore
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.max_node = 0
        self.inorder(root)
        return self.max_node                
    def inorder(self, node):
        if not node:
            return ([], True)
        (left_result, left_success) = self.inorder(node.left)
        (right_result, right_success) = self.inorder(node.right)
        if not left_success or not right_success:
            return ([], False)
        if right_result and node.val >= right_result[0]:
            return ([], False)
        if left_result and node.val <= left_result[-1]:
            return ([], False)
        result = left_result + [node.val] + right_result
        self.max_node = max(self.max_node, len(result))
        return (result, True)