class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [[] for i in range(2048)]
        self.capacity = 2048
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key%self.capacity
        for in_idx in range(len(self.array[index])):
            in_key = self.array[index][in_idx][0]
            if in_key == key:
                self.array[index][in_idx] = (key, value)
                return
        self.array[index].append((key, value))
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.capacity
        for in_key, value in self.array[index]:
            if in_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key%self.capacity
        for in_idx in range(len(self.array[index])):
            in_key = self.array[index][in_idx][0]
            if in_key == key:
                self.array[index].pop(in_idx)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)