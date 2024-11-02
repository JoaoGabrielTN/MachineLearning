import numpy as np

def actions_function(state):
     actions = []
     zero_pos = np.argwhere(state == 0)[0]
     x, y = zero_pos

     # Possible moves: Up, Down, Left, Right
     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
     for dx, dy in directions:
         new_x, new_y = x + dx, y + dy
         if 0 <= new_x < 3 and 0 <= new_y < 3:  # Check boundaries
             actions.append((new_x, new_y))

def move(state, action):
    # Find the position of the empty tile (0)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                x, y = i, j
                break

    # Calculate the new position based on the action
    new_x, new_y = x + action[0], y + action[1]

    # Check if the new position is within the bounds
    if 0 <= new_x < len(state) and 0 <= new_y < len(state[0]):
        # Create a copy of the state to avoid modifying the original
        new_state = [row.copy() for row in state]

        # Swap the empty tile with the tile at the new position
        new_state[x][y] = state[new_x][new_y]
        new_state[new_x][new_y] = 0

        return new_state
    else:
        # Invalid move, return the original state
        return state


def result_modify(s, a):
    # Apply the action to the state
  s = move(s, a)

  # Store the resulting state
  result = copy.deepcopy(s)

  return result

def result_copy(s, a):
    # Create a deep copy of the state
  s_copy = copy.deepcopy(s)

  # Apply the action to the copy
  s_copy = move(s_copy, a)

  return s_copy

def iddfs_copy(s, goal):
  depth = 0
  while True:
      result = dls_copy(s, goal, depth)
      if result is not None:
          return result
      depth += 1

def dls_copy(s, goal, depth):
    if s == goal:
        return s
    elif depth <= 0:
        return None
    else:
        for a in actions_function(s):
            result = dls_copy(result_copy(s, a), goal, depth - 1)
            if result is not None:
                return result
    return None

def iddfs_modify_undo(s, goal):
    depth = 0
    while True:
        result = dls_modify(s, goal, depth)
        if result is not None:
           return result
        depth += 1

def dls_modify(s, goal, depth):
    if s.all() == goal.all():
        return s
    elif depth <= 0:
        return None
    else:
        for a in actions_function(s):
            result = dls_modify(result_modify_undo(s, a), goal, depth - 1)
            if result is not None:
                return result
    return None

if __name__ == "__main__":
    initial_state = np.array([[3, 2, 1],
                              [4, 0, 5],
                              [7, 6, 8]])

    goal_state = np.array([[1, 2, 3],
                           [4, 0, 5],
                           [7, 8, 0]])

    depth = 5
    print(iddfs_modify_undo(initial_state, goal_state))
    print(dls_modify(initial_state, goal_state, depth))
