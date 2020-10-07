#BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.childTable = [[] for i in range(numCourses)]
        self.dependNumTable = [0 for i in range(numCourses)]
        
        for dependancy in prerequisites:
            parent = dependancy[1]
            child = dependancy[0]
            self.childTable[parent].append(child)
            self.dependNumTable[child] += 1

        result = []
        queue = []
        for numCourse in range(numCourses):
            if self.dependNumTable[numCourse] == 0:
                queue.append(numCourse)
        while len(queue) > 0:
            course = queue.pop(0)
            result.append(course)
            for child in self.childTable[course]:
                self.dependNumTable[child] -= 1
                if self.dependNumTable[child] == 0:
                    queue.append(child)
                    
        return result if len(result) == numCourses else []

#DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.status_table = ["unvisited" for i in range(numCourses)]
        self.child_table = [[] for j in range(numCourses)]
        result = []
        for dependency in prerequisites:
            parent = dependency[1]
            child = dependency[0]
            self.child_table[parent].append(child)
        
        for idx in range(len(self.status_table)):
            if self.status_table[idx] == "unvisited":
                if not self.helper(idx, result):
                    return []
        return reversed(result)
    
    def helper(self, course, result):
        if self.status_table[course] == "visiting":
            return False
        self.status_table[course] = "visiting"
        for child in self.child_table[course]:
            if self.status_table[child] == "visited":
                continue
            if not self.helper(child, result):
                return False
        result.append(course)
        self.status_table[course] = "visited"
        return True

# DFS, build reverse table
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        child_table = {}
        status_table = {}
        ans =[]
        for num in range(numCourses):
            child_table[num] = []
            status_table[num] = "unvisited"
        self.buildChildTable(child_table, prerequisites)
        for num in range(numCourses):
            if status_table[num] == "visited":
                continue
            if not self.helper(status_table, child_table, num, ans):
                return []
        return ans
    
    def helper(self, status_table, child_table, num, ans):
        if status_table[num] == "visiting":
            return False
        status_table[num] = "visiting"
        for child in child_table[num]:
            if status_table[child] == "visited":
                continue
            if not self.helper(status_table, child_table, child, ans):
                return False
        ans.append(num)
        status_table[num] = "visited"
        return True

    def buildChildTable(self, table, prerequisites):
        for dependancy in prerequisites:
            table[dependancy[0]].append(dependancy[1])