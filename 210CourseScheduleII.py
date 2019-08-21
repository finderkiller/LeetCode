#BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.depend_table = {}
        self.child_table = {}
        
        course_list = []
        for idx in range(numCourses):
            self.depend_table[idx] = 0
            self.child_table[idx] = []
            course_list.append(idx)
        for dependence in prerequisites:
            self.buildChildTable(dependence)
            self.buildDependTable(dependence)
            
        result = []
        order = []
        self.buildNoDependCourse(course_list, order)
        
        while len(order) > 0:
            current = order.pop(0)
            result.append(current)
            for child in self.child_table[current]:
                self.depend_table[child] -= 1
            self.buildNoDependCourse(self.child_table[current], order)
            
        return result if len(result) == numCourses else []
        
        
        
    def buildNoDependCourse(self, course_list, order):
        for idx, data in enumerate(course_list):
            if self.depend_table[data] == 0:
                order.append(data)
            
            
    def buildChildTable(self, pair):
        if not pair:
            return
        parent = pair[1]
        child = pair[0]
        self.child_table[parent].append(child)
    
    def buildDependTable(self, pair):
        if not pair:
            return
        parent = pair[1]
        child = pair[0]
        self.depend_table[child] += 1

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