#combination in k spot, meaning 9!/(9-k)!*k!. and each combination cost O(k) copy to result, so
#time: O(9!*k/(9-k)!*k!), space: O(k), depth: O(k)

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        collection = []
        result = []
        self.helper(collection, 1, n, result, k)
        return result
        
    def helper(self, collection, start, target, result, k):
        if sum(collection) == target and len(collection) == k:
            result.append(list(collection))
            return
        if len(collection) > k:
            return
        if sum(collection) > target:
            return
        for num in range(start, 10):
            collection.append(num)
            self.helper(collection, num+1, target, result, k)
            collection.pop()

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        collect = []
        result = []
        self.helper(collect, 1, 0, n, k, result)
        return result
        
    def helper(self, collect, start, current, target, k, result):
        if len(collect) > k:
            return
        if current == target and len(collect) == k:
            result.append(list(collect))
            return
        if current == target:
            return
        if start * (k-len(collect)) > target-current:
            return
        for num in range(start, 10):
            collect.append(num)
            self.helper(collect, num+1, current+num, target, k, result)
            collect.pop()