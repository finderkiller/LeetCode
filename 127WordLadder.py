"""
1. build table:
    *ot: hot, 
    h*t: hot, 
    ho*: hot, 
    
2. traverse from beginWord, separate it letter by letter, hit-> *it, h*t, hi*,
using those three words to find the key in the table
a. if word == endWord, return 1

3. BFS
"""
#BFS, with build *table, hit-> *it, h*t, hi*
#time: O(N*S^2), space: O(N*S^2), S is the length of words

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.table = {}                     #O(n*s*s)
        for word in wordList:               #O(n*s*s)
            for idx in range(len(word)):
                key = word[:idx] + "*" + word[idx+1:]
                if key not in self.table:
                    self.table[key] = []
                self.table[key].append(word)
        
        step = 1
        queue = []
        visited = set()
        for idx in range(len(beginWord)):
            queue.append(beginWord[:idx] + "*" + beginWord[idx+1:])
            visited.add(beginWord[:idx] + "*" + beginWord[idx+1:])
        
        while len(queue) > 0:
            next_queue = []
            for next_key in queue:
                for next_word in self.table.get(next_key, []):
                    if next_word == endWord:
                        return step+1
                    for idx in range(len(next_word)):
                        key = next_word[:idx] + "*" + next_word[idx+1:]
                        if key in visited:
                            continue
                        next_queue.append(key)
                        visited.add(key)
            queue = next_queue
            step += 1
        
        return 0

#BFS, traverse 26 alphabet
#time: O(N*26^S), space: O(N), S is the length of words

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.table = set(wordList)
        queue = []
        queue.append(beginWord)
        self.visited = set()
        self.visited.add(beginWord)
        step = 1
        while len(queue) > 0:
            next_queue = []
            for word in queue:
                for idx in range(len(word)):
                    for alpha in range(0, 26):
                        next_word = word[:idx] + chr(ord('a')+alpha) + word[idx+1:]
                        if next_word in self.visited:
                            continue
                        if next_word not in self.table:
                            continue
                        if next_word == endWord:
                            return step + 1
                        self.visited.add(next_word) 
                        next_queue.append(next_word)
            queue = next_queue
            step += 1
        return 0

#BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.table = set(wordList)
        queue = []
        queue.append(beginWord)
        step = 1
        while len(queue) > 0:
            next_queue = []
            for word in queue:
                for idx in range(len(word)):
                    for alpha in range(0, 26):
                        next_word = word[:idx] + chr(ord('a')+alpha) + word[idx+1:]
                        if next_word not in self.table:
                            continue
                        if next_word == endWord:
                            return step + 1
                        self.table.remove(next_word)
                        next_queue.append(next_word)
            queue = next_queue
            step += 1
        return 0
            