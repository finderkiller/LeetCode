class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        people = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
        for idx in range(len(people)):
            pair = people[idx]
            k = pair[1]
            if k == idx:
                continue
            people.pop(idx)
            people.insert(k, pair)
        return people
        
        