#snap time: O(n), timeoout, when n is too large
"""
1. cur array
2. snap_id from 0
3. table, snap_id: copy_array

"""
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [0 for i in range(length)]
        self.table = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.table[self.snap_id] = list(self.array)
        ret = self.snap_id
        self.snap_id += 1
        return ret

    def get(self, index: int, snap_id: int) -> int:
        if snap_id not in self.table:
            return 0
        return self.table.get(snap_id)[index]

#snap time: O(length of set action)
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_table = {}
        self.set_table = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.set_table[index] = val

    def snap(self) -> int:
        self.snap_table[self.snap_id] = dict(self.set_table)
        ret = self.snap_id
        self.snap_id += 1
        return ret

    def get(self, index: int, snap_id: int) -> int:
        set_table = self.snap_table[snap_id]
        return set_table.get(index, 0)