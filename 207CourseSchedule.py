#DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_list = []
        self.status_table = {}
        self.child_table = {}
        for idx in range(numCourses):
            self.status_table[idx] = "UNVISITED"
            self.child_table[idx] = []
            course_list.append(idx)
        for dependence in prerequisites:
            self.buildChildTable(dependence)
    
        for course in course_list:
            if self.status_table[course] != "UNVISITED":
                continue
            if not self.helper(course):
                return False
        return True
               
    def helper(self, course):
        if self.status_table[course] == "VISITING":
            return False
        if self.status_table[course] == "VISITED":
            return True
        
        self.status_table[course] = "VISITING"
        for child in self.child_table[course]:
            if not self.helper(child):
                return False
        self.status_table[course] = "VISITED"
        return True
        
    def buildChildTable(self, pair):
        if not pair:
            return
        parent = pair[1]
        child = pair[0]
        self.child_table[parent].append(child)
    