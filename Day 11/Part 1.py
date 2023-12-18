'''
For part 1 and 2 change col and row sum amount between 1 and 1000000 - 1 respectively
'''
import numpy as np

def calculate_manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

lines = open("Day 11/inputs.txt").read().splitlines()
grid = np.array([[c for c in line] for line in lines])
double_rows = [i for i in range(len(grid)) if '#' not in grid[i]]
double_cols = [i for i in range(len(grid[0]) - 1) if '#' not in grid[:,i]]
galaxy_pos = list(zip(*np.where(grid == "#")))

distances = []
for i, p in enumerate(galaxy_pos):
    for j, q in enumerate(galaxy_pos):
        #Only count each pair once
        if p == q or j < i:
            continue

        #Get unscaled distance
        distance = calculate_manhattan_distance(p, q)

        #Add for each empty row and col moved through
        distance += sum([1000000 - 1 for row in double_rows if min(p[0], q[0]) < row < max(p[0], q[0])])
        distance += sum([1000000 - 1 for col in double_cols if min(p[1], q[1]) < col < max(p[1], q[1])])

        #print(f"distance between galaxy {i} and galaxy {j}: {distance}")
        distances.append(distance)

print(sum(distances))
