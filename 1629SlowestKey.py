class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_time = releaseTimes[0]
        result = keysPressed[0]
        for idx in range(1, len(keysPressed)):
            if releaseTimes[idx] - releaseTimes[idx-1] > max_time:
                max_time = releaseTimes[idx] - releaseTimes[idx-1] 
                result = keysPressed[idx]
            elif releaseTimes[idx] - releaseTimes[idx-1] == max_time and keysPressed[idx] > result:
                result = keysPressed[idx]
        return result