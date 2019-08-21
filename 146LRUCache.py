# using table and array
class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.capacity = capacity
        self.order = []
        

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        self.changeorder(key)
        return self.table[key]

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.table[key] = value
            return
        if len(self.order) == self.capacity:
            self.table.pop(self.order[0])
            self.order.pop(0)
        self.table[key] = value
        self.order.append(key)
    def changeorder(self, key):
        for idx, value in enumerate(self.order):
            if value == key:
                self.order = self.order[:idx] + self.order[idx+1:]
                self.order.append(key)
                return
# using table and Double LinkedList
class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.node_table = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.node_table.pop(node.key)
        self.size -=1

    def add_node_head(self, node): #add node always at head
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
        self.node_table[node.key] = node
        self.size += 1

    def pop_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node
    
    def get(self, key):
        if self.size == 0:
            return -1
        if key not in self.node_table:
            return -1
        node = self.node_table[key]
        self.remove_node(node)
        self.add_node_head(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return
        if self.get(key) != -1:
            node = self.node_table[key]
            node.val = value
            return
        if self.size == self.capacity:
            self.pop_tail()
        new_node = Node(key, value)
        self.add_node_head(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)