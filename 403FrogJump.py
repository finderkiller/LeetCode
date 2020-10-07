class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return True
        stone_set = set(stones)
        step_table = {}
        step_table[stones[0]] = set([1])
        
        for stone in stones:
            if stone not in step_table:
                continue
            steps = step_table[stone]
            for step in steps:
                if (stone+step) not in stone_set:
                    continue
                if stone+step not in step_table:
                    step_table[stone+step] = set()
                step_table[stone+step].add(step+1)
                if step > 0:
                    step_table[stone+step].add(step)
                if step > 1:
                    step_table[stone+step].add(step-1)
        return stones[-1] in step_table