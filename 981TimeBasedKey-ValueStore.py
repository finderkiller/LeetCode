class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_table ={}
        self.key_time_table={}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.key_table:
            self.key_table[key] = []
        
        self.key_table[key].append(timestamp)
        self.key_time_table[(key, timestamp)] = value        
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if (key, timestamp) in self.key_time_table:
            return self.key_time_table[(key, timestamp)]
        if key not in self.key_table:
            return
        array = self.key_table[key]
        import bisect
        insert_point = bisect.bisect_right(array, timestamp)
        if insert_point == 0:
            return ""
        return self.key_time_table[(key, array[insert_point-1])]