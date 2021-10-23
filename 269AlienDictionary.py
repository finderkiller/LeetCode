#time: O(n*L), space: O(n*L)
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        table = {}
        ans = []
        status_table = {}
        for word in words:
            for char in word:
                status_table[char] = "unvisited"
                table[char] = []
        for idx in range(1, len(words)):
            prev_word = words[idx-1]
            cur_word = words[idx]
            i = 0
            while i < len(prev_word) and i < len(cur_word):
                if prev_word[i] == cur_word[i]:
                    i += 1
                    continue
                table[cur_word[i]].append(prev_word[i])
                break
        for key in table.keys():
            if status_table[key] == "visited":
                continue
            if not self.helper(table, status_table, key, ans):
                return ""
        return "".join(ans)
    def helper(self, table, status_table, key, ans):   
        if status_table[key] == "visiting":
            return False
        status_table[key] = "visiting"
        for child in table[key]:
            if status_table[child] == "visited":
                continue
            if not self.helper(table, status_table, child, ans):
                return False
        ans.append(key)
        status_table[key] = "visited"
        return True