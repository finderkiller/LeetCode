# brute force, time: O(3^n)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        return self.helper(costs, 0, -1)
        
    def helper(self, costs, start, color_pre):
        if start == len(costs):
            return 0
        result = sys.maxsize
        for idx, cost in enumerate(costs[start]):
            if idx == color_pre:
                continue
            result = min(result, cost+self.helper(costs, start+1, idx))
        return result

# memo, time: O(n), space: O(n), depth: O(n)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        self.table = {}
        return self.helper(costs, 0, -1)
        
    def helper(self, costs, start, color_pre):
        if start == len(costs):
            return 0
        if (start, color_pre) in self.table:
            return self.table[(start, color_pre)]
        result = sys.maxsize
        for idx, cost in enumerate(costs[start]):
            if idx == color_pre:
                continue
            result = min(result, cost+self.helper(costs, start+1, idx))
        self.table[(start, color_pre)] = result
        return self.table[(start, color_pre)]

#bottom up: time:O(n), space: O(n)
 class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        self.table = [[sys.maxsize for i in range(3)] for i in range(len(costs))]
        for idx in range(len(self.table)):
            for color in range(3):
                if idx == 0:
                    self.table[idx][color] = costs[idx][color]
                    continue
                if color == 0:
                    self.table[idx][color] = min(self.table[idx][color], \
                                             costs[idx][color] + self.table[idx-1][color+1], \
                                             costs[idx][color] + self.table[idx-1][color+2])
                elif color == 1:
                    self.table[idx][color] = min(self.table[idx][color], \
                                             costs[idx][color] + self.table[idx-1][color-1], \
                                             costs[idx][color] + self.table[idx-1][color+1])
                else:
                    self.table[idx][color] = min(self.table[idx][color], \
                                             costs[idx][color] + self.table[idx-1][color-2], \
                                             costs[idx][color] + self.table[idx-1][color-1])
        return min(self.table[-1])

#bottom up: time:O(n), space: O(1)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        pre_result = []
        for idx in range(len(costs)):
            current_result = [sys.maxsize for i in range(3)]
            for color in range(3):
                if idx == 0:
                    current_result[color] = costs[idx][color]
                    continue
                if color == 0:
                    current_result[color] = min(current_result[color], \
                                             costs[idx][color] + pre_result[color+1], \
                                             costs[idx][color] + pre_result[color+2])
                elif color == 1:
                    current_result[color] = min(current_result[color], \
                                             costs[idx][color] + pre_result[color-1], \
                                             costs[idx][color] + pre_result[color+1])
                else:
                    current_result[color] = min(current_result[color], \
                                             costs[idx][color] + pre_result[color-2], \
                                             costs[idx][color] + pre_result[color-1])
            pre_result = current_result
        return min(pre_result)