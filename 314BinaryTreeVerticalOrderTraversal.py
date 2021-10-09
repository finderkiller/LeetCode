#time: O(n), space: 
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        collection = {}
        result = []
        queue = []
        queue.append((root,0))
        while len(queue) > 0:
            child_list = []
            for node, index in queue:
                if index not in collection:
                    collection[index] = []
                collection[index].append(node.val)
                if node.left:
                    child_list.append((node.left, index-1))
                if node.right:
                    child_list.append((node.right, index+1))
            queue = child_list
        for idx in sorted(collection.keys()):
            result.append(collection[idx])
        return result