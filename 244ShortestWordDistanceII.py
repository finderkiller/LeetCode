#O(n^2)
class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.table = {}
        for idx, word in enumerate(wordsDict):
            if word not in self.table:
                self.table[word] = []
            self.table[word].append(idx)
        

    def shortest(self, word1: str, word2: str) -> int:
        word1_idx_list = self.table.get(word1)
        word2_idx_list = self.table.get(word2)
        result = sys.maxsize
        for idx1 in word1_idx_list:
            for idx2 in word2_idx_list:
                result = min(result, abs(idx1-idx2))
        return result


#O(n)
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.table = {}
        for idx, word in enumerate(wordsDict):
            if word not in self.table:
                self.table[word] = []
            self.table[word].append(idx)
        

    def shortest(self, word1: str, word2: str) -> int:
        word1_idx_list = self.table.get(word1)
        word2_idx_list = self.table.get(word2)
        result = sys.maxsize
        i = j = 0
        while i < len(word1_idx_list) and j < len(word2_idx_list):
            dist = word1_idx_list[i] - word2_idx_list[j]
            result = min(result, abs(dist))
            if dist < 0:
                i += 1
            else:
                j += 1
        return result