class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.visited = set()
        self.direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.helper(robot, 0, 0, 0)
        
        
    def helper(self, robot, row, col, dir):
        robot.clean()
        self.visited.add((row, col))
        for idx in range(4):
            cur_idx = (dir+idx)%4
            next_row = row + self.direction[cur_idx][0]
            next_col = col + self.direction[cur_idx][1]
            if (next_row, next_col) not in self.visited and robot.move():
                self.helper(robot, next_row, next_col, cur_idx)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnRight()