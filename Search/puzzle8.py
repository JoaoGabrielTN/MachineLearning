import numpy as np
import time
import copy

def actions_function(state):
    actions = []
    zero_pos = np.argwhere(state == 0)[0]
    x, y = zero_pos

    # Possible moves: Up, Down, Left, Right
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:  # Check boundaries
            actions.append((dx, dy))  # Return direction as action

    return actions

def move(state, action):
    # Find the position of the empty tile (0)
    zero_pos = np.argwhere(state == 0)[0]
    x, y = zero_pos
    dx, dy = action

    # Calculate the new position based on the action
    new_x, new_y = x + dx, y + dy

    # Check if the new position is within the bounds
    if 0 <= new_x < len(state) and 0 <= new_y < len(state[0]):
        # Create a copy of the state to avoid modifying the original
        new_state = state.copy()
        # Swap the empty tile with the tile at the new position
        new_state[x, y], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[x, y]
        return new_state
    else:
        # Invalid move, return the original state
        return state

def result_copy(s, a):
    # Create a deep copy of the state and apply the action
    s_copy = copy.deepcopy(s)
    return move(s_copy, a)

def dfs_copy(s, goal, depth):
    if np.array_equal(s, goal):
        return s
    elif depth <= 0:
        return None
    else:
        for a in actions_function(s):
            result = dfs_copy(result_copy(s, a), goal, depth - 1)
            if result is not None:
                return result
    return None

def iddfs_copy(s, goal):
    depth = 0
    while True:
        result = dfs_copy(s, goal, depth)
        if result is not None:
            return result
        depth += 1

if __name__ == "__main__":
    initial_state = np.array([[1, 2, 3], [4, 5, 0], [7, 8, 6]])
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    depth = 5

    start_time_copy = time.time()
    iddfs_solution = iddfs_copy(initial_state, goal_state)
    end_time_copy = time.time()

    start_time_modify_undo = time.time()
    dls_solution= dfs_copy(initial_state, goal_state, depth)
    end_time_modify_undo = time.time()

    print("Initial state:\n", initial_state, end='\n')
    print("Goal state:\n", goal_state, end='\n')
    print("Time taken using iddfs:", end_time_copy - start_time_copy, end='\n')
    print("Solution:\n", iddfs_solution, end="\n")
    print("")
    print("Time taken using dfs:", end_time_modify_undo - start_time_modify_undo, end='\n')
    print("Solution:\n", dls_solution)
