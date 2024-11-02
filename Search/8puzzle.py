from queue import PriorityQueue
import numpy as np

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state 
        self.parent = parent  
        self.action = action  
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions_function(self, state):
        actions = []
        zero_pos = np.argwhere(state == 0)[0]  
        x, y = zero_pos

        # Possible moves: Up, Down, Left, Right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:  # Check boundaries
                actions.append((new_x, new_y))

        return actions

    def result_function(self, state, action):
        new_state = state.copy()
        x, y = np.argwhere(state == 0)[0]
        new_x, new_y = action
        new_state[x, y], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[x, y]
        return new_state

    def goal_test(self, state):
        return np.array_equal(state, self.goal_state)

    def step_cost_function(self, action):
        return 1  

class AStarSearch:
    def search(self, problem):
        frontier = PriorityQueue()
        start_node = Node(problem.initial_state, path_cost=0)
        frontier.put((0, start_node))
        explored = set()

        while not frontier.empty():
            current_cost, current_node = frontier.get()

            if problem.goal_test(current_node.state):
                return self.get_solution(current_node)

            explored.add(tuple(map(tuple, current_node.state)))

            for action in problem.actions_function(current_node.state):
                child_state = problem.result_function(current_node.state, action)
                if tuple(map(tuple, child_state)) not in explored:
                    new_cost = current_node.path_cost + problem.step_cost_function(action)
                    child_node = Node(child_state, current_node, action, new_cost)
                    priority = new_cost + self.heuristic(child_node)
                    frontier.put((priority, child_node))

        return None

    def heuristic(self, node):
        goal_positions = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                          3: (1, 0), 4: (1, 1), 5: (1, 2),
                          6: (2, 0), 7: (2, 1), 8: (2, 2)}
        distance = 0
        for number in range(1, 9): 
            current_pos = np.argwhere(node.state == number)[0]
            goal_pos = goal_positions[number]
            distance += abs(current_pos[0] - goal_pos[0]) + abs(current_pos[1] - goal_pos[1])
        return distance

    def get_solution(self, node):
        actions = []
        while node.parent is not None:
            actions.append(node.action)
            node = node.parent
        return actions[::-1] 

if __name__ == "__main__":
    initial_state = np.array([[3, 2, 1],
                               [4, 0, 5],
                               [7, 6, 8]])
    goal_state = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 0]])

    problem = Problem(initial_state, goal_state)
    search = AStarSearch()
    solution = search.search(problem)

    if solution:
        print("Solution found! Actions to reach the goal:")
        for action in solution:
            print(action)
    else:
        print("No solution found.")
