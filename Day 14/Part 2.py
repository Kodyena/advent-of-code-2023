grid =  open("Day 14/inputs.txt").read().splitlines()
#Rotate grid by 90 to make manips easier so N is E
grid = list(zip(*grid[::-1]))
grid = [''.join(row) for row in grid]

def move_rocks(grid: list[str]):
    new_grid = []
    for row in grid:
        sections = row.split('#')
        new_sections = []
        for section in sections:
            n = section.count('O')
            new_sections.append('.' * (len(section) - n) + 'O' * n)
        new_grid.append("#".join(new_sections))
    return new_grid

def calculate_load(grid: list[str]) :
    loads = [sum([i + 1 for i, char in enumerate(row) if char == 'O']) for row in grid]
    return sum(loads)

def rotate_grid(grid: list[str]):
    grid = list(zip(*grid[::-1]))
    return [''.join(row) for row in grid]

def cycle_grid(grid: list[str]):
    for _ in range(4):
        grid = move_rocks(grid)
        grid = rotate_grid(grid)
    return grid

'''
Peform the n cycles keeping a history of the grid after every cycle.
As the process is linear if we detect the current state in the grid history the system will loop.
Calculate the point inside the loop by finding the remainder of the loop length on the remaining cycles.
'''
n = 1000000000
grid_history = []
for i in range(n):
    grid = cycle_grid(grid)
    flat_grid = '\n'.join(grid)
    if flat_grid in grid_history:
        loop_start = grid_history.index(flat_grid)
        #Find remainder of how many cycles can fit in remaining n
        r = ((n - loop_start) % (i - loop_start))
        grid = grid_history[r + loop_start - 1].splitlines()
        break
    else:
        grid_history.append(flat_grid)

print(calculate_load(grid))