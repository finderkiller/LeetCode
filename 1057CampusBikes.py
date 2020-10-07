#brute Force O(n*n*m)
class Solution(object):
    def assignBikes(self, workers, bikes):
        output = [0 for i in range(len(workers))]
        table = [[0 for i in range(len(workers))] for j in range(len(bikes))]
        for bike_idx, bike in enumerate(bikes):
            for idx, worker in enumerate(workers):
                distance = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
                table[bike_idx][idx] = distance
        count = len(workers)
        while count > 0:
            min_distance = sys.maxsize
            candidate_bike = -1
            candidate_worker = -1
            for bike_idx in range(len(table)):     
                for worker_idx in range(len(table[0])):
                    if table[bike_idx][worker_idx] == -1:
                        continue
                    if table[bike_idx][worker_idx] < min_distance:
                        min_distance = table[bike_idx][worker_idx]
                        candidate_bike = bike_idx
                        candidate_worker = worker_idx
            output[candidate_worker] = candidate_bike
            for worker_idx in range(len(table[0])):
                table[candidate_bike][worker_idx] = -1
            for bike_idx in range(len(table)):
                table[bike_idx][candidate_worker] = -1
            count -= 1
        return output
        
#sort all distance, O(n*m * log(n*m))
class Solution(object):
    def assignBikes(self, workers, bikes):
        output = [0 for i in range(len(workers))]
        worker_visited = set()
        bike_visited = set()
        table = []
        for bike_idx, bike in enumerate(bikes):
            for worker_idx, worker in enumerate(workers):
                distance = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
                table.append([distance, bike_idx, worker_idx])
        table = sorted(table, key=lambda x:x[0])
        for data in table:
            distance = data[0]
            bike = data[1]
            worker = data[2]
            if bike in bike_visited or worker in worker_visited:
                continue
            output[worker] = bike
            worker_visited.add(worker)
            bike_visited.add(bike)
        return output
#bucket sort, using distance as key, O(n*m)
class Solution(object):
    def assignBikes(self, workers, bikes):
        output = [0 for i in range(len(workers))]
        worker_visited = set()
        bike_visited = set()
        table = {}
        for bike_idx, bike in enumerate(bikes):
            for worker_idx, worker in enumerate(workers):
                distance = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
                if distance in table:
                    table[distance].append((bike_idx, worker_idx))
                else:
                    table[distance] = [(bike_idx, worker_idx)]
        for distance, array in sorted(table.iteritems(), key=lambda x:x[0]):
            for data in array:
                bike = data[0]
                worker = data[1]
                if bike in bike_visited or worker in worker_visited:
                    continue
                output[worker] = bike
                worker_visited.add(worker)
                bike_visited.add(bike)
        return output
#bucket sort, using distance as index, O(n*m)
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        output = [0 for i in range(len(workers))]
        worker_visited = set()
        bike_visited = set()
        table = [[] for i in range(2001)]
        for bike_idx, bike in enumerate(bikes):
            for worker_idx, worker in enumerate(workers):
                distance = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
                table[distance].append((bike_idx, worker_idx))
        for array in table:
            for data in array:
                bike = data[0]
                worker = data[1]
                if bike in bike_visited or worker in worker_visited:
                    continue
                output[worker] = bike
                worker_visited.add(worker)
                bike_visited.add(bike)
        return output
                
        
                
        