#O(n)
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_idx_list = []
        word2_idx_list = []
        for idx, word in enumerate(wordsDict):
            if word == word1:
                word1_idx_list.append(idx)
            if word == word2:
                word2_idx_list.append(idx)
                
        result = sys.maxsize
        if word1 == word2:
            for idx in range(1, len(word1_idx_list)):
                result = min(result, word1_idx_list[idx]-word1_idx_list[idx-1])
        else:
            i = j = 0
            while i < len(word1_idx_list) and j < len(word2_idx_list):
                dist = word1_idx_list[i] - word2_idx_list[j]
                result = min(result, abs(dist))
                if dist < 0:
                    i += 1
                else:
                    j += 1
        return result