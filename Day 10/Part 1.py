import numpy as np
'''
Need to navigate grid and take route that leads from and back to S
-Keep note of all previous points moved into. If an adjacent tile has not been explored then move into it.
-Move onto all possible tiles simultaneously, keep a queue structure of each tile and route. Include the number of moves to get there.
-Possible moves are represented by a dict, check cardinal direction of tile being moved in is contained within that value. i.e S is in tile value if moving south.
-In data structure need to include list of tile location and previous move

-NB Moving East is +ve x, moving North is -ve y
-A Move is: (x, y, previous move)
'''
grid = np.array([list(line) for line in open("Day 10/inputs.txt").read().splitlines()])
pipe_to_directions = {
    '|': 'NS',
    '-': 'EW',
    'L': 'NE',
    'J': 'NW',
    '7': 'SW',
    'F' : 'SE',
    '.': '',
    'S': 'NWSE',
}
move_directions = ['N', 'E', 'S', 'W']
direction_to_xy = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
pipe_connections = {'N': 'S', 'E':'W', 'S':'N', 'W':'E'}

def check_pipes_connected(direction: str, pipe: str):
    connecting_pipe = pipe_connections.get(direction)
    return connecting_pipe in pipe_to_directions.get(pipe)

def get_loop(grid):
    #Find start position
    start_y, start_x = np.where(grid=='S')
    start_x = start_x[0]
    start_y = start_y[0]

    #Iterate until loop found adding routes to a structure to keep checking
    routes = [' ', [(start_x, start_y)]]
    while True:
        if len(routes) == 0: return None
        route = routes.pop()
        last_direction = route[0]
        x, y = route[-1]
        for direction in [d for d in pipe_to_directions.get(grid[y,x]) if d != last_direction]:
            y_mov, x_mov = direction_to_xy.get(direction)
            new_x = x + x_mov
            new_y = y + y_mov
            if(not 0 <= new_x < len(grid[0]) or not 0 <= new_y < len(grid)):
                continue
            next_pipe = grid[new_y, new_x]
            if(len(route) >= 4 and next_pipe == 'S'):
                return route
            if not check_pipes_connected(direction, next_pipe):
                continue
            elif (new_x, new_y) in route[-1][-2]:
                continue

            updated_route = route.copy()
            updated_route.append((new_x, new_y))
            routes.append(updated_route)
 

print((len(get_loop(grid)) // 2))