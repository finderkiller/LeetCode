#top-down memo, time: O(N*L^2), space: O(N)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.word_set = set(words)
        self.table = {}
        result = 0
        for word in words:
            result = max(result, self.helper(word))
        return result
        
    def helper(self, word):
        if not word:
            return 0
        if word in self.table:
            return self.table[word]
        result = 0
        for idx in range(len(word)):
            if word[:idx] + word[idx+1:] not in self.word_set:
                continue
            result = max(result, self.helper(word[:idx] + word[idx+1:]))
        self.table[word] = result+1
        return self.table[word]