class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) != len(cost):
            return -1
        cur_gas = 0
        total_gas = 0
        start = 0
        for idx in range(len(gas)):
            if cur_gas + gas[idx] < cost[idx]:
                cur_gas = 0
                start = idx+1
            else:
                cur_gas = cur_gas + gas[idx] - cost[idx]
            total_gas = total_gas + gas[idx] - cost[idx]
        return start if total_gas >= 0 else -1