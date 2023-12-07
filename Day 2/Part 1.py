import re

n_of_cubes = [12, 13, 14]

with open('Day 2\input.txt') as f:
    id_count = 0
    for line in f:
        game_id = int(re.findall('Game (\d+)', line)[0])
        max_red = max([int(n) for n in re.findall('(\d+) red', line)], default=0)
        max_blue = max([int(n) for n in re.findall('(\d+) blue', line)], default=0)
        max_green = max([int(n) for n in re.findall('(\d+) green', line)], default=0)
        if max_red <= n_of_cubes[0] and max_green <= n_of_cubes[1] and max_blue <= n_of_cubes[2]:
            id_count += game_id
print(id_count)