class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost:
            return -1
        if len(gas) != len(cost):
            return -1
        total = 0
        start = 0
        temp = 0
        for idx in range(len(gas)):
            total += gas[idx] - cost[idx]
            temp += gas[idx] - cost[idx]
            if temp <0:
                start = idx+1
                temp = 0
        return start if total >=0 else -1
            