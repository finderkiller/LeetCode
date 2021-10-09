# memo, time: O(n*k), space: O(n*k), depth: O(n)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
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

# DP, time: O(n*k*k), space: O(n*k), depth: O(n)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        pre_result = []
        for idx in range(len(costs)):
            current_result = [sys.maxsize for i in range(len(costs[0]))]
            for color in range(len(costs[0])):
                if idx == 0:
                    current_result[color] = costs[idx][color]
                    continue
                for pre_color in range(len(costs[0])):
                    if pre_color == color:
                        continue
                    current_result[color] = min(current_result[color], \
                                             costs[idx][color] + pre_result[pre_color])
            pre_result = current_result
        return min(pre_result)

# DP, time: O(n*k), space: O(1)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        pre_result = []
        for idx in range(len(costs)):
            if idx == 0:
                current_result = costs[idx]
                pre_result = current_result
                continue
            pre_min_cost = min(pre_result)
            current_result = [0 for i in range(len(costs[0]))]
            for color in range(len(costs[0])):
                if pre_result[color] == pre_min_cost:
                    temp = pre_result[color]
                    pre_result[color] = math.inf
                    current_result[color] = costs[idx][color] + min(pre_result)
                    pre_result[color] = temp
                else:
                    current_result[color] = costs[idx][color] + pre_min_cost
            pre_result = current_result
        return min(pre_result)