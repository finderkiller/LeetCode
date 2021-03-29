class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.word_set = set(words)
        self.table = {}
        result = []
        for word in words:
            if word == "":
                continue
            self.word_set.remove(word)
            if self.helper(word, 0):
                result.append(word)
            self.word_set.add(word)
        return result
    def helper(self, word, start):
        if word[start:] in self.word_set:
            return True
        if word[start:] in self.table:
            return self.table[word[start:]]
        for idx in range(start, len(word)):
            string = word[start:idx+1]
            if string not in self.word_set:
                continue
            if self.helper(word, idx+1):
                self.table[word[start:]] = True
                return True
        self.table[word[start:]] = False
        return False