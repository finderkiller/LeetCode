#DFS
# time: O(N*P),  Each of N searches could search the entire graph.
# #space: O(P)
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        graph = {}
        for pair in similarPairs:
            w1 = pair[0]
            w2 = pair[1]
            if w1 not in graph:
                graph[w1] = []
            if w2 not in graph:
                graph[w2] = []
            graph[w1].append(w2)
            graph[w2].append(w1)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            self.visited = set()
            if not self.helper(w1, w2, graph):
                return False
        return True
    def helper(self, string, target, graph):
        if not string:
            return False
        if string == target:
            return True
        if string not in graph:
            return False
        self.visited.add(string)
        for child in graph[string]:
            if child in self.visited:
                continue
            if self.helper(child, target, graph):
                return True
        return False
#BFS
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        graph = {}
        for pair in similarPairs:
            w1 = pair[0]
            w2 = pair[1]
            if w1 not in graph:
                graph[w1] = []
            if w2 not in graph:
                graph[w2] = []
            graph[w1].append(w2)
            graph[w2].append(w1)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            visited = set()
            visited.add(w1)
            queue = [w1]
            found = False
            while len(queue) > 0:
                next_queue = []
                for word in queue:
                    if word == w2:
                        found = True
                        break
                    for child in graph.get(word, []):
                        if child in visited:
                            continue
                        visited.add(child)
                        next_queue.append(child)
                queue = next_queue
                if found:
                    break
            if not found:
                return False
        return True