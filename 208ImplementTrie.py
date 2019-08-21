class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndofWord = False
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def charToIndex(self, char):
        return ord(char) - ord('a')
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        pointer = self.root
        length = len(word)
        for level in range(length):
            char = word[level]
            index = self.charToIndex(char)
            if not pointer.children[index]:
                pointer.children[index] = TrieNode()
            pointer = pointer.children[index]
        pointer.isEndofWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return True
        pointer = self.root
        length = len(word)
        for level in range(length):
            char = word[level]
            index = self.charToIndex(char)
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]
        return pointer != None and pointer.isEndofWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True
        pointer = self.root
        length = len(prefix)
        for level in range(length):
            char = prefix[level]
            index = self.charToIndex(char)
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]
        return pointer != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)