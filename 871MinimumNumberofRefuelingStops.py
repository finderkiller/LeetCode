#memo
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        self.table = {}
        result = self.helper(stations, 0, startFuel, 0, target)
        return result if result != sys.maxsize else -1
        
        
    def helper(self, stations, start, cur_fuel, cur_miles, target):
        if cur_miles+cur_fuel >= target:
            return 0
        if (start, cur_fuel, cur_miles) in self.table:
            return self.table[(start, cur_fuel, cur_miles)]
        result = sys.maxsize
        for idx in range(start, len(stations)):
            miles = stations[idx][0]
            gas = stations[idx][1]
            if cur_miles + cur_fuel < miles:
                break
            forward = self.helper(stations, idx+1, cur_fuel+cur_miles-miles+gas, miles, target)
            if forward != -1:
                result = min(result, forward+1)
        self.table[(start, cur_fuel, cur_miles)] = result if result != sys.maxsize else -1
        return self.table[(start, cur_fuel, cur_miles)]

