class Node:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
    def convert(self, char):
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.root
        for char in word:
            if not ptr.children[self.convert(char)]:
                ptr.children[self.convert(char)] = Node()
            ptr = ptr.children[self.convert(char)]
        ptr.is_end = True
        
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.root
        for char in word:
            if not ptr.children[self.convert(char)]:
                return False
            ptr = ptr.children[self.convert(char)]
        return ptr.is_end
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.root
        for char in prefix:
            if not ptr.children[self.convert(char)]:
                return False
            ptr = ptr.children[self.convert(char)]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)