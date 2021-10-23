#DFS time:O(v+E), space: O(V+E), depth: O(V)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.child_table = {}
        self.visited_table = {}
        for course in range(numCourses):
            self.visited_table[course] = "unvisited"
        
        for child, parent in prerequisites:
            if parent not in self.child_table:
                self.child_table[parent] = []
            self.child_table[parent].append(child)
            
        for course in range(numCourses):
            if self.visited_table[course] == "visited":
                continue
            if not self.helper(course):
                return False
        return True
        
    def helper(self, course):
        self.visited_table[course] = "visiting"
        for child in self.child_table.get(course, []):
            if self.visited_table[child] == "visited":
                continue
            if self.visited_table[child] == "visiting":
                return False
            if not self.helper(child):
                return False
        self.visited_table[course] = "visited"
        return True