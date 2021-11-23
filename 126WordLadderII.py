class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.table = set(wordList)
        if beginWord in self.table:
            self.table.remove(beginWord)
        self.depend_table = {}
        queue = set()
        queue.add(beginWord)
        found = False
        while len(queue) > 0 and not found:
            next_queue = set()
            for word in queue:
                if word not in self.depend_table:
                    self.depend_table[word] = []
                for idx in range(len(word)):
                    for alpha in range(0, 26):
                        next_word = word[:idx] + chr(ord('a')+alpha) + word[idx+1:]
                        if next_word == word:
                            continue
                        if next_word not in self.table:
                            continue
                        if next_word == endWord:
                            self.depend_table[word].append(next_word)
                            found = True
                        elif not found:
                            self.depend_table[word].append(next_word)
                            next_queue.add(next_word)
            for word in next_queue:
                self.table.remove(word)
            queue = next_queue
        if not found:
            return []
        collection = [beginWord]
        result = []
        self.helper(collection, beginWord, endWord, result)
        return result

    def helper(self, collection, word, target, result):
        if word == target:
            result.append(list(collection))
            return
        for next_word in self.depend_table.get(word, []):
            collection.append(next_word)
            self.helper(collection, next_word, target, result)
            collection.pop()