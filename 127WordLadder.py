class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        depend_table = defaultdict(list)
        for idx in range(len(beginWord)):
            depend_table[beginWord[:idx] + '*' + beginWord[idx+1:]].append(beginWord)
        for word in wordList:
            for idx in range(len(word)):
                depend_table[word[:idx] + '*' + word[idx+1:]].append(word)
        level = 1
        visit = set() 
        current_queue = []
        for idx in range(len(beginWord)):
            visit.add(beginWord[:idx] + '*' + beginWord[idx+1:])
            current_queue.append(beginWord[:idx] + '*' + beginWord[idx+1:])
            
        while len(current_queue) > 0:
            child_queue = []
            for key in current_queue:
                for word in depend_table.get(key):
                    if word == endWord:
                        return level+1
                    for idx in range(len(word)):
                        child = word[:idx] + '*' + word[idx+1:]
                        if child in visit:
                            continue
                        visit.add(child)
                        child_queue.append(child)
            current_queue = child_queue
            level += 1
        return 0