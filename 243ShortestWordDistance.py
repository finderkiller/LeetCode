#O(n^2)
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        table = {}
        for idx, word in enumerate(wordsDict):
            if word not in table:
                table[word] = []
            table[word].append(idx)
        word1_idx_list = table.get(word1)
        word2_idx_list = table.get(word2)
        min_dist = len(wordsDict)
        for idx1 in word1_idx_list:
            for idx2 in word2_idx_list:
                min_dist = min(min_dist, abs(idx1-idx2))
        return min_dist


#O(n)
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_idx_list = []
        word2_idx_list = []
        for idx, word in enumerate(wordsDict):
            if word == word1:
                word1_idx_list.append(idx)
            elif word == word2:
                word2_idx_list.append(idx)
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
        