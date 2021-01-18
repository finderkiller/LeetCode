class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        username_table = defaultdict(list)
        for idx in range(len(username)):
            username_table[username[idx]].append((timestamp[idx], website[idx]))
        for name, values in username_table.items():
            values.sort(key = lambda x:x[0])
        table = defaultdict(int)
        for name, values in username_table.items():
            sub_set = set()
            right = 2
            while right < len(values):
                for first in range(0, right-1):
                    for second in range(first+1, right):
                        if (values[first][1], values[second][1], values[right][1]) in sub_set:
                            continue
                        table[(values[first][1], values[second][1], values[right][1])] += 1
                        sub_set.add((values[first][1], values[second][1], values[right][1]))
                right += 1
        max_count = 0
        result = ""
        for sequence, count in table.items():
            if count > max_count:
                max_count = count
                result = [sequence[0], sequence[1], sequence[2]]
            elif count == max_count and sequence[0] < result[0]:
                result = [sequence[0], sequence[1], sequence[2]]
            elif count == max_count and sequence[0] == result[0] and sequence[1] < result[1]:
                result = [sequence[0], sequence[1], sequence[2]]
            elif count == max_count and sequence[0] == result[0] and sequence[1] == result[1] and sequence[2] < result[2]:
                result = [sequence[0], sequence[1], sequence[2]]
        return result
                
            