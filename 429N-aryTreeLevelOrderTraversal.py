#BFS
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        current = [root]
        while len(current) > 0:
            parent_list = current
            current = []
            collect = []
            for parent in parent_list:
                collect.append(parent.val)
                for child in parent.children:
                    current.append(child)
            result.append(list(collect))
        return result

#DFS
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        self.helper(root, 0, result)
        return result
    def helper(self, node, level, result):
        if not node:
            return
        if len(result) == level:
            result.append([node.val])
        else:
            result[level].append(node.val)
        for child in node.children:
            self.helper(child, level+1, result)