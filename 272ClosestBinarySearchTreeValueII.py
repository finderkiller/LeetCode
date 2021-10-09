# O(klogn)
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            return []
        self.pq = []
        self.helper(root, target)
        import heapq
        self.get_result(root, target)
        result = []
        while k > 0:
            dist, value = heapq.heappop(self.pq)
            result.append(int(value))
            k -= 1
        return result
        
    def helper(self, node, target):
        if not node:
            return
        node.val = node.val - target
        self.helper(node.left, target)
        self.helper(node.right, target)
        
    def get_result(self, node, target):
        if not node:
            return
        heapq.heappush(self.pq, (abs(node.val), node.val+target))
        self.get_result(node.left, target)
        self.get_result(node.right, target)

#O(n), inorder traverse, find insert point and use two pointer

# O(logn + k)
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            return []
        result = []
        collection_forward = []
        collection_backward = []
        self.forward(root, collection_forward, target, k)
        self.backward(root, collection_backward, target, k)
        while len(result) < k:
            if len(collection_forward) == 0:
                result.append(collection_backward.pop(0))
            elif len(collection_backward) == 0:
                result.append(collection_forward.pop(0))
            elif abs(collection_forward[0]-target) < abs(collection_backward[0]-target):
                result.append(collection_forward.pop(0))
            else:
                result.append(collection_backward.pop(0))
        return result
    
    def forward(self, node, collection_forward, target, k):
        if not node:
            return
        if len(collection_forward) == k:
            return
        if node.val >= target:
            self.forward(node.left, collection_forward, target, k)
            if len(collection_forward) == k:
                return
            collection_forward.append(node.val)
        self.forward(node.right, collection_forward, target, k)
        
    def backward(self, node, collection_backward, target, k):
        if not node:
            return
        if len(collection_backward) == k:
            return
        if node.val < target:
            self.backward(node.right, collection_backward, target, k)
            if len(collection_backward) == k:
                return
            collection_backward.append(node.val)
        self.backward(node.left, collection_backward, target, k)
        