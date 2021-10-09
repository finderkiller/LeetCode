# hash_table
class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        #O(1)
        if key not in self.table:
            self.table[key] = 0
        self.table[key] += 1
        
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        #O(1)
        self.table[key] -= 1
        if self.table[key] == 0:
            self.table.pop(key)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        #O(n)
        max_count = -sys.maxsize-1
        max_key = ""
        for key, count in self.table.items():
            if count > max_count:
                max_key = key
                max_count = count
        return max_key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        #O(n)
        min_count = sys.maxsize
        min_key = ""
        for key, count in self.table.items():
            if count < min_count:
                min_key = key
                min_count = count
        return min_key

#Double Linked List + has_table
class Node:
    def __init__(self, key, count):
        self.key = key
        self.count = count
        self.pre = None
        self.next = None
class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}
        self.head = Node("", 0)
        self.tail = Node("", sys.maxsize)
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        #O(n)
        if key not in self.table:
            node = Node(key, 1)
            self.table[key] = node
        else:
            node = self.table.get(key)
            self.remove_node(node)
            node.count += 1
        self.insert_node(node)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        #O(n)
        node = self.table.get(key)
        self.remove_node(node)
        node.count -= 1
        if node.count > 0:
            self.insert_node(node)
        else:
            self.table.pop(key)
        
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        #O(1)
        max_node = self.tail.pre
        return max_node.key
        
    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        #O(1)
        min_node = self.head.next
        return min_node.key
    
    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.next = None
                
    def insert_node(self, node):
        ptr = self.head
        while ptr and ptr.next:
            if ptr.next.count > node.count:
                node.next = ptr.next
                node.pre = ptr.next.pre
                ptr.next = node
                node.next.pre = node
                break
            ptr = ptr.next

#Double Linked List + (freq,node) hash_table + (key,freq) hash_table
class Node:
    def __init__(self, freq):
        self.freq = freq
        self.words = set()
        self.pre = None
        self.next = None
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.key_table = {}
        self.freq_table = {}
        
    def add_to_freq(self, key, freq):
        if freq == 0:
            return
        if freq not in self.freq_table:
            node = Node(freq)
            node.words.add(key)
            self.freq_table[freq] = node
            if freq == 1:
                self.insert_after(self.head, node)
            elif freq-1 in self.freq_table:
                self.insert_after(self.freq_table[freq-1], node)
            elif freq+1 in self.freq_table:
                self.insert_after(self.freq_table[freq+1].pre, node)
        else:
            node = self.freq_table[freq]
            node.words.add(key)
            
    def remove_from_freq(self, key, freq):
        node = self.freq_table[freq]
        node.words.remove(key)
        if len(node.words) == 0:
            self.remove_node(node)
            self.freq_table.pop(freq)
            
    def insert_after(self, ptr, node):
        node.next = ptr.next
        node.pre = ptr
        ptr.next = node
        node.next.pre = node
    
    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.next = None
            
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        #O(1)
        if key not in self.key_table:
            self.key_table[key] = 1
            self.add_to_freq(key, 1)
        else:
            self.add_to_freq(key, self.key_table[key]+1)
            self.key_table[key] += 1
            self.remove_from_freq(key, self.key_table[key]-1)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        #O(1)
        self.add_to_freq(key, self.key_table[key]-1)
        self.key_table[key] -= 1
        self.remove_from_freq(key, self.key_table[key]+1)
        if self.key_table[key] == 0:
            self.key_table.pop(key)
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        #O(1)
        if len(self.tail.pre.words) == 0:
            return ""
        return list(self.tail.pre.words)[0]
        
    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        #O(1)
        if len(self.head.next.words) == 0:
            return ""
        return list(self.head.next.words)[0]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()