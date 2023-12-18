import numpy as np

'''
Part1:
Need to navigate grid and take route that leads from and back to S
-Keep note of all previous points moved into. If an adjacent tile has not been explored then move into it.
-Move onto all possible tiles simultaneously, keep a queue structure of each tile and route. Include the number of moves to get there.
-Possible moves are represented by a dict, check cardinal direction of tile being moved in is contained within that value. i.e S is in tile value if moving south.
-In data structure need to include list of tile location and previous move

-NB Moving East is +ve x, moving North is -ve y
-A Move is: (x, y, previous move)
Part2:
Determine if a tile is in a loop by iterating through row by row
-Wait to hit a loop tile, then accumulate non loop tiles
-When you hit a second loop tile add to list of inner tiles and repeat
OR
-Order the list of loop tiles into lists of rows (ordered again by column)
-Remove adjacent loop tiles so we only have the terminating verticies
-For each pair in each row, calculate the difference in column number
-Add to count
'''
grid = np.array([list(line) for line in open("Day 10/test.txt").read().splitlines()])
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
            elif (new_x, new_y) in route:
                continue

            updated_route = route.copy()
            updated_route.append((new_x, new_y))
            routes.append(updated_route)
 
def get_loop_inner_tiles(loop):
    column_numbers = set([n[0] for n in loop])
    rows = [sorted([n[1] for n in loop if n[0] == i]) for i in column_numbers]
    count = 0
    for row in rows:
        differences = [d - 1 for n in zip(row, row[1:]) if (d := n[1] - n[0]) > 1]
        count += sum([d for i, d in enumerate(differences) if i % 2 == 0])
    return count           

def subtract_xy(xy1: tuple[int, int], xy2: tuple[int, int]):
    return (xy1[0] - xy2[0], xy1[1] - xy2[1])

def get_inner_tile_count(loop):
    #Get verticies
    verts = [loop[i] for i in range(len(loop)) if(subtract_xy(loop[(i + 1) % len(loop)], loop[i]) != subtract_xy(loop[i], loop[(i - 1) % len(loop)]))]
    
    #Get area using Shoelace formula
    #print(verts)
    area = 0
    for i in range(len(verts) - 1):
        v0 = verts[i]
        v1 = verts[i + 1 % len(verts)]
        area += v0[0] * v1[1] - v1[0] * v0[1]
    area *= 0.5
    print(area)
    #Get number of interior spaces using Pick's formula
    #Using equation i = A - b/2 +1
    return int(area - (len(loop) / 2) + 1)

print(get_inner_tile_count(get_loop(grid)))